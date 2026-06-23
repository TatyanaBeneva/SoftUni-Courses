searched_book = input()
new_book = input()
checked_books_count = 0

while new_book != 'No More Books':
    if new_book == searched_book:
        print(f"You checked {checked_books_count} books and found it.")
        break

    checked_books_count += 1
    new_book = input()
else:
    print("The book you search is not here!")
    print(f"You checked {checked_books_count} books.")


