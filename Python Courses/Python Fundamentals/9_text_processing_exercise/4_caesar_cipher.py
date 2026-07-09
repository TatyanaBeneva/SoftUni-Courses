text = input()
encrypted_text = ""

for char in text:
    next_char = chr(ord(char) + 3)
    encrypted_text += next_char

print(encrypted_text)