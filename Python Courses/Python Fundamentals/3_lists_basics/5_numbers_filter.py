n = int(input())
numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

command = input()
filtered_numbers = []

if command == "even":
    for number in numbers:
        if number % 2 == 0:
            filtered_numbers.append(number)
elif command == "odd":
    for number in numbers:
        if number % 2 != 0:
            filtered_numbers.append(number)
elif command == "negative":
    for number in numbers:
        if number < 0:
            filtered_numbers.append(number)
elif command == "positive":
    for number in numbers:
        if number >= 0:
            filtered_numbers.append(number)

print(filtered_numbers)