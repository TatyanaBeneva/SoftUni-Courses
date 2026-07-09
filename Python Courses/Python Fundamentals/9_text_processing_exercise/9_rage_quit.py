text = input()

sequence = ""
number = ""
new_text = ""

for char in text:
    if char.isdigit():
        number += char
    else:
        if number:
            new_text += sequence * int(number)
            sequence = ""
            number = ""

        sequence += char.upper()

if number:
    new_text += sequence * int(number)

unique_symbols = len(set(new_text))

print(f"Unique symbols used: {unique_symbols}")
print(new_text)