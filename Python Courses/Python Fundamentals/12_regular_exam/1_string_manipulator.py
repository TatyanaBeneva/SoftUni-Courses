text = input()

while True:
    command = input()

    if command == "End":
        break

    command = command.split()
    action = command[0]

    if action == "Translate":
        char = command[1]
        replacement = command[2]
        text = text.replace(char, replacement)
        print(text)

    elif action == "Includes":
        substring = command[1]

        if text.find(substring) == -1:
            print("False")
        else:
            print("True")

    elif action == "Start":
        substring = command[1]
        print(text.startswith(substring))

    elif action == "Lowercase":
        text = text.lower()
        print(text)

    elif action == "FindIndex":
        char = command[1]
        index = text.rfind(char)
        print(index)

    elif action == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        last_index = start_index + count

        if last_index <= len(text) and (0 <= start_index <= len(text)):
            text_to_remove = text[start_index:start_index + count]
            text = text.replace(text_to_remove, "")
            print(text)
