number_of_messages = int(input())

for message in range(number_of_messages):
    current_number = int(input())
    current_message = ""

    if current_number == 88:
        current_message = "Hello"
    elif current_number == 86:
        current_message = "How are you?"
    elif current_number < 88:
        current_message = "GREAT!"
    elif current_number > 88:
        current_message = "Bye."

    print(current_message)