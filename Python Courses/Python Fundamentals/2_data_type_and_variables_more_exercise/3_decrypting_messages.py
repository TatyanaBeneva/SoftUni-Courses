key = int(input())
number_of_lines = int(input())
encrypted_message = ""

for i in range(number_of_lines):
    letter = input()
    encrypted_letter = chr(ord(letter) + key)
    encrypted_message += encrypted_letter

print(encrypted_message)



