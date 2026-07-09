text = input()
new_text = ""
left_strength = 0

for i, char in enumerate(text):
    if char == ">":
        left_strength += int(text[i + 1])

    if left_strength > 0 and char.isalnum():
        left_strength -= 1
    else:
        new_text += char

print(new_text)