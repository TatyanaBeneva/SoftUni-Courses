def main():
    n = int(input())

    for _ in range(n):
        command, text = input().split(":")

        if is_command_valid(command) and is_translator_valid(text):
            message = f"{command[1:-1]}:"
            for i in range(1, len(text)-1):
                message += f" {ord(text[i])}"

            print(message)
        else:
            print("The message is invalid")

def is_command_valid(command):
    if (command.startswith("!")
            and command.endswith("!")
            and command[1].isupper()
            and command[2:].islower()
            and len(command) >= 3):
        return True

    return False

def is_translator_valid(text):
    if (text.startswith("[")
            and text.endswith("]")
            and text[1:-1].isalpha()
            and len(text) >= 8):
        return True

    return False
main()