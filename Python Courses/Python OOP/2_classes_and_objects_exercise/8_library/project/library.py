from project.user import User


class Library:
    def __init__(self) -> None:
        self.user_records: list[User] = []
        self.books_available: dict[str, list[str]] = {}
        self.rented_books: dict[str, dict[str, int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str | None:
        if book_name in self.books_available.get(author, []):
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            self.rented_books.setdefault(user.username, {})[book_name] = days_to_return

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for username, books in self.rented_books.items():
            if book_name in books:
                return (
                    f'The book "{book_name}" is already rented and '
                    f'will be available in {books[book_name]} days!'
                )

        return None

    def return_book(self, author: str, book_name: str, user: User) -> str | None:
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]