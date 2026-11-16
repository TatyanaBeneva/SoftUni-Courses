class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"{self.title} from {self.author}"

class Library:
    def __init__(self, *args):
        self.books = []
        if args:
            self.books = args

    def find_book(self, title):
        book = next((book for book in self.books if book.title == title), None)

        if book is None:
            return f"Book {title} doesn't exist"
        else:
            return book