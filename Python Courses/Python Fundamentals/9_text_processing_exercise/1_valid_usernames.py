def main():
    usernames = input().split(", ")

    for username in usernames:
        if is_valid(username):
            print(username)


def is_valid(username: str) -> bool:
    if not 3 <= len(username) <= 16:
        return False

    for char in username:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False

    return True


main()