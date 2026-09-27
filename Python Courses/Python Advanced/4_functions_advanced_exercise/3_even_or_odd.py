def even_odd(*args):
    result = []
    command = args[-1]
    numbers = args[:-1]

    if command == "even":
        result = [el for el in numbers if el % 2 == 0]
    elif command == "odd":
        result = [el for el in numbers if el % 2 != 0]

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
