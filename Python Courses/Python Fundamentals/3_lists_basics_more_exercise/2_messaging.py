numbers = input().split(" ")
some_string = input()
message = ""

for sequence in numbers:
    index = 0

    for string in sequence:
        number = int(string)
        index += number

    valid_index = index % len(some_string)
    message += some_string[valid_index]
    new_text = some_string[:valid_index] + some_string[valid_index + 1:]
    some_string = new_text

print(message)