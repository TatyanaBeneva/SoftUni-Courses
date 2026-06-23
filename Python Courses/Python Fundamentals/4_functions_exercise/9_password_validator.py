def is_between_6_10_chars(string: str):
    if  6 <= len(string) <= 10:
        return True

def is_letter_and_digits(string: str):
    for char in string:
        if not char.isalpha() and not char.isdigit():
            return False
    return True

def is_have_at_least_2_digits(string: str):
    counter = 0
    for char in string:
        if char.isdigit():
            counter += 1
            if counter == 2:
                return True
    return False

def is_password_valid(password: str):
    if not is_between_6_10_chars(password):
        print("Password must be between 6 and 10 characters")

    if not is_letter_and_digits(password):
        print("Password must consist only of letters and digits")

    if not is_have_at_least_2_digits(password):
        print("Password must have at least 2 digits")

    if is_between_6_10_chars(password) and\
            is_letter_and_digits(password) and\
            is_have_at_least_2_digits(password):
        print("Password is valid")

password = input()
is_password_valid(password)
