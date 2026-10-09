from tkinter import Canvas, TclError, messagebox
from tkinter.ttk import Button, Frame, Label, Scrollbar

from .helpers import clean_screen
from .canvas import tk
from . import storage


def logout():
    from .authentication import render_main_enter_screen
    render_main_enter_screen()


def render_products():
    clean_screen()
    Button(tk, text="Log out", command=logout).pack(anchor="ne", padx=8, pady=8)
    try:
        products = storage.read_records("products.txt")
    except (OSError, ValueError) as error:
        messagebox.showerror("Cannot load products", str(error), parent=tk)
        return
    if not products:
        Label(tk, text="No products available.").pack(pady=20)
        return

    container = Frame(tk)
    container.pack(fill="both", expand=True)
    canvas = Canvas(container, highlightthickness=0)
    scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    catalog = Frame(canvas)
    window = canvas.create_window((0, 0), window=catalog, anchor="nw")
    catalog.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>", lambda event: canvas.itemconfigure(window, width=event.width))
    for column in range(4):
        catalog.columnconfigure(column, weight=1, uniform="products")

    for index, product in enumerate(products):
        row, column = divmod(index, 4)
        item = Frame(catalog, padding=8)
        item.grid(row=row, column=column, sticky="nsew")
        Label(item, text=product["name"], wraplength=130).pack()
        image_label = Label(item, text="No image available", anchor="center")
        image_label.pack(pady=8)
        try:
            from PIL import Image, ImageTk
            with Image.open(storage.BASE_DIR / "images" / product.get("img_path", "")) as image:
                photo = ImageTk.PhotoImage(image.resize((100, 100)), master=tk)
            image_label.configure(image=photo, text="")
            image_label.image = photo
        except (ImportError, OSError, ValueError, TclError):
            pass
        Label(item, text=f"In stock: {product['count']}").pack(pady=2)
        Button(item, text="Buy", command=lambda product_id=product["id"]: buy_product(product_id),
               state="normal" if product["count"] > 0 else "disabled").pack()


def buy_product(product_id):
    try:
        storage.purchase(product_id)
    except (OSError, ValueError, KeyError) as error:
        messagebox.showerror("Purchase failed", str(error), parent=tk)
    render_products()
