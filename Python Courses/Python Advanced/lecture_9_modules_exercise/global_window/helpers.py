from .canvas import tk


def clean_screen():
    for widget in tk.winfo_children():
        widget.destroy()
