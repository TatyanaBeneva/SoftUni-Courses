name = input()
result = ""
is_successful = True

while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        is_successful = False
        break

    if len(name) < 5:
        result = f"{name} goes to Gryffindor."
    elif len(name) == 5:
        result = f"{name} goes to Slytherin."
    elif len(name) == 6:
        result = f"{name} goes to Ravenclaw."
    elif len(name) > 6:
        result = f"{name} goes to Hufflepuff."

    print(result)
    name = input()

if is_successful:
    print("Welcome to Hogwarts.")