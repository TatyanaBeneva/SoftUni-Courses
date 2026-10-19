import json
import tkinter as tk
from PIL import Image, ImageTk
import os

from canvas import app
from helpers import clean_screen


base_folder = os.path.dirname(os.path.abspath(__file__))


def update_current_user(username, product_id):
    with open(os.path.join(base_folder, "db", "users.txt"), "r+") as file:
        users = [json.loads(user.strip()) for user in file]

        for user in users:
            if user["username"] == username:
                user["products"].append(product_id)
                file.seek(0)
                file.truncate()
                file.writelines(json.dumps(user) + "\n" for user in users)
                return

def purchase_product(product_id):
    with open(os.path.join(base_folder, "db", "products.txt"), "r+") as file:
        products = [json.loads(product.strip()) for product in file]

        for product in products:
            if product["id"] == product_id:
                product["count"] -= 1
                file.seek(0)
                file.truncate()
                file.writelines(json.dumps(product) + "\n" for product in products)
                return

def buy_product(product_id):
    clean_screen()

    with open(os.path.join(base_folder, "db", "current_user.txt")) as file:
        username = file.read().strip()

    if username:
        update_current_user(username, product_id)
        purchase_product(product_id)

    render_products_screen()

def add_product(name, image, count):
    with open("db/products.txt", "r+") as file:
        if name == "" or image == "" or count == "":
            render_add_product_screen(error="All fields are required!")
            return
        if not count.isdigit():
            render_add_product_screen(error="Count must be a valid number!")
            return

        file.write(json.dumps({
            "id": len(file.readlines()) + 1,
            "name": name,
            "img_path": image,
            "count": int(count)}) + "\n")

        render_products_screen()

def render_add_product_screen(error=None):
    clean_screen()

    tk.Label(app, text="Name: ").grid(row=0, column=0)
    name = tk.Entry(app)
    name.grid(row=0, column=1)

    tk.Label(app, text="Image: ").grid(row=1, column=0)
    image = tk.Entry(app)
    image.grid(row=1, column=1)

    tk.Label(app, text="Count: ").grid(row=2, column=0)
    count = tk.Entry(app)
    count.grid(row=2, column=1)

    tk.Button(
        app,
        text="Add",
        command=lambda: add_product(name.get(), image.get(), count.get()),
    ).grid(row=3, column=0)

    if error:
        tk.Label(app, text=error).grid(row=4, column=0)


def render_products_screen():
    clean_screen()

    with open(os.path.join(base_folder, "db", "products.txt")) as file:
        products = [json.loads(product.strip()) for product in file]
        products = [product for product in products if product["count"] > 0]
        products_per_row = 6
        rows_for_product = len(products[0])

        for i, product in enumerate(products):
            row = (i // products_per_row) * rows_for_product
            column = i % products_per_row

            tk.Label(app, text=product["name"]).grid(row=row, column=column)

            img = Image.open(os.path.join(base_folder, "db", "images", product["img_path"])).resize((100, 100))
            photo_image = ImageTk.PhotoImage(img)
            image_label = tk.Label(app, image=photo_image)
            image_label.image = photo_image
            image_label.grid(row=row+1, column=column)

            tk.Label(app, text=product["count"]).grid(row=row+2, column=column)
            tk.Button(
                app,
                text=f"Buy {product['id']}",
                command=lambda product_id=product["id"]: buy_product(product_id),
            ).grid(row=row+3, column=column)

            with open("db/current_user.txt") as file:
                username = file.read().strip()

            with open("db/users.txt") as file:
                users = [json.loads(user.strip()) for user in file]

                for user in users:
                    if user["username"] == username:
                        if user.get("is_admin"):
                            tk.Button(
                                app,
                                text="Add product",
                                bg="green",
                                fg="white",
                                command=render_add_product_screen
                            ).grid(row=row+4, column=0)

                        break
