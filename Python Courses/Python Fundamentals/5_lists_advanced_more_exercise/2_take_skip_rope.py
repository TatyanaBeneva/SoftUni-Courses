def destructure_strings_numbers(string):
    numbers = [num for num in string if num.isdigit()]
    chars = [char for char in string if not char.isdigit()]

    return numbers, chars

def destructure_numbers_list(numbers_list):
    take_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 == 0 ]
    skip_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 != 0 ]

    return take_list, skip_list

def decrypt_message(string_list, take_list, skip_list):
    message = ""
    string = "".join(string_list)

    for i in range(len(take_list)):
        message += string[:take_list[i]]
        string = string[take_list[i] + skip_list[i]:]

    return message



message_input = input()

number_list, char_list = destructure_strings_numbers(message_input)
take_char_list, skip_char_list = destructure_numbers_list(number_list)
decrypted_message = decrypt_message(char_list, take_char_list, skip_char_list)

print(decrypted_message)
