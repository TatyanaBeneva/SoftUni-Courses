from tkinter import Button, Entry, Label, messagebox

from .canvas import tk
from .helpers import clean_screen
from .products import render_products
from . import storage


def login(username, pword):
    try:
        valid = storage.authenticate(username, pword)
    except (OSError, ValueError, KeyError) as error:
        messagebox.showerror("Login failed", str(error), parent=tk)
        return
    if valid:
        render_products()
    else:
        render_login(error="Invalid username or password")


def register(**user):
    try:
        storage.create_user(**user)
    except (OSError, ValueError, KeyError) as error:
        messagebox.showerror("Registration failed", str(error), parent=tk)
        return
    render_login()


def add_field(label, row, secret=False):
    Label(tk, text=label).grid(row=row, column=0, sticky="w", padx=8, pady=6)
    entry = Entry(tk, show="*" if secret else "")
    entry.grid(row=row, column=1, padx=8, pady=6)
    return entry


def render_login(error=None):
    clean_screen()
    username = add_field("Username", 0)
    password = add_field("Password", 1, secret=True)
    username.focus_set()
    Button(tk, text="Enter", bg="green", fg="white",
           command=lambda: login(username.get(), password.get())).grid(row=2, column=1)
    Button(tk, text="Back", command=render_main_enter_screen).grid(row=2, column=0)
    if error:
        Label(tk, text=error, fg="red").grid(row=3, column=0, columnspan=2)


def render_register():
    clean_screen()
    username = add_field("Username", 0)
    password = add_field("Password", 1, secret=True)
    first_name = add_field("First name", 2)
    last_name = add_field("Last name", 3)
    username.focus_set()
    Button(tk, text="Register", bg="green", fg="white",
           command=lambda: register(username=username.get(), password=password.get(),
                                    first_name=first_name.get(), last_name=last_name.get())
           ).grid(row=4, column=1)
    Button(tk, text="Back", command=render_main_enter_screen).grid(row=4, column=0)


def render_main_enter_screen():
    storage.current_user = None
    clean_screen()
    Button(tk, text="Login", bg="green", fg="white", command=render_login).grid(row=0, column=0)
    Button(tk, text="Register", bg="yellow", fg="black", command=render_register).grid(row=0, column=1)
