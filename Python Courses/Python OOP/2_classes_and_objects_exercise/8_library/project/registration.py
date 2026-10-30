from project.library import Library
from project.user import User


class Registration:
    def add_user(self, user: User, library: Library) -> str | None:
        if any(u.user_id == user.user_id for u in library.user_records):
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)
        return None

    def remove_user(self, user: User, library: Library) -> str | None:
        existing_user = next((u for u in library.user_records if u.user_id == user.user_id), None)

        if existing_user is None:
            return "We could not find such user to remove!"

        library.user_records.remove(existing_user)
        return None

    def change_username(self, user_id: int, new_username: str, library: Library) -> str:
        user = next((user for user in library.user_records if user.user_id == user_id), None)

        if user is None:
            return f"There is no user with id = {user_id}!"

        if user.username == new_username:
            return f"Please check again the provided username - it should be different than the username used so far!"

        old_username = user.username

        if old_username in library.rented_books:
            library.rented_books[new_username] = library.rented_books.pop(old_username)

        user.username = new_username

        user.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"