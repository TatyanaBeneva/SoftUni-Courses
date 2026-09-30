import os

while True:
    command = input().split("-")

    if command == ["End"]:
        break

    action = command[0]
    file_name = command[1]

    if action == "Create":
        with open(file_name, "w") as file:
            file.write("")

    elif action == "Add":
        content = command[2]
        with open(file_name, "a") as file:
            file.write(f"{content}\n")

    elif action == "Replace":
        old_string = command[2]
        new_string = command[3]

        try:
            with open(file_name, "r") as file:
                content = file.read()
            with open(file_name, "w") as file:
                file.write(content.replace(old_string, new_string))
        except FileNotFoundError:
            print("An error occurred")
            continue

    elif action == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
            continue
