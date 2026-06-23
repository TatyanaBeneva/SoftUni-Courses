import sys

max_number = -sys.maxsize

while True:
    new_input = input()

    if new_input == "Stop":
        break

    number = int(new_input)

    if number > max_number:
        max_number = number

print(max_number)