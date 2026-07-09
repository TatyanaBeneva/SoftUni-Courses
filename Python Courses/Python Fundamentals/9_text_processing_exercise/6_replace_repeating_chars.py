text = input()
new_text = ""
current_char = ""

for char in text:
    if char != current_char:
        current_char = char
        new_text += current_char

print(new_text)