import sys

min_number = sys.maxsize

while True:
    new_input = input()

    if new_input == "Stop":
        break

    number = int(new_input)

    if number < min_number:
        min_number = number

print(min_number)