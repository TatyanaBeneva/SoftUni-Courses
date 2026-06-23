round_number = lambda x: round(x)

numbers = list(map(float ,input().split()))
rounded_numbers = []

for number in numbers:
    ronded_number = round_number(number)
    rounded_numbers.append(ronded_number)

print(rounded_numbers)