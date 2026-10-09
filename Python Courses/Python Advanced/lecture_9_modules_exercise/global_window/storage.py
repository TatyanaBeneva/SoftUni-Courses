import hashlib
import hmac
import json
import os
from pathlib import Path
import re
import tempfile


BASE_DIR = Path(__file__).resolve().parent
DB_DIR = BASE_DIR / "db"
current_user = None


def read_records(name):
    path = DB_DIR / name
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def write_records(name, records):
    DB_DIR.mkdir(parents=True, exist_ok=True)
    # Replace a complete file so shorter records cannot leave trailing data.
    fd, temporary = tempfile.mkstemp(dir=DB_DIR, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as file:
            for record in records:
                file.write(json.dumps(record) + "\n")
        os.replace(temporary, DB_DIR / name)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def create_user(username, password, first_name, last_name):
    username = username.strip()
    first_name, last_name = first_name.strip(), last_name.strip()
    if not re.fullmatch(r"[A-Za-z0-9_]{3,30}", username):
        raise ValueError("Username must contain 3-30 letters, digits or underscores.")
    if len(password) < 8 or not password.strip():
        raise ValueError("Password must contain at least 8 characters.")
    if not all(1 <= len(name) <= 50 for name in (first_name, last_name)):
        raise ValueError("First and last names must contain 1-50 characters.")
    users = read_records("users.txt")
    if any(user["username"].casefold() == username.casefold() for user in users):
        raise ValueError("This username is already registered.")
    salt = os.urandom(16).hex()
    password_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), bytes.fromhex(salt), 600_000
    ).hex()
    users.append(dict(username=username, first_name=first_name, last_name=last_name,
                      salt=salt, password_hash=password_hash, products=[]))
    write_records("users.txt", users)


def authenticate(username, password):
    global current_user
    current_user = None
    for user in read_records("users.txt"):
        if user["username"].casefold() != username.strip().casefold():
            continue
        digest = hashlib.pbkdf2_hmac(
            "sha256", password.encode(), bytes.fromhex(user["salt"]), 600_000
        ).hex()
        if hmac.compare_digest(digest, user["password_hash"]):
            current_user = user["username"]
            return True
    return False


def purchase(product_id):
    users = read_records("users.txt")
    user = next((user for user in users if user["username"] == current_user), None)
    if user is None:
        raise ValueError("Please log in before buying a product.")
    products = read_records("products.txt")
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        raise ValueError("This product is no longer available.")
    if product["count"] <= 0:
        raise ValueError("This product is out of stock.")
    product["count"] -= 1
    user["products"].append(product_id)
    write_records("products.txt", products)
    try:
        write_records("users.txt", users)
    except OSError:
        product["count"] += 1
        write_records("products.txt", products)
        raise
