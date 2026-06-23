moves = int(input())

points = 0.0
first_range = 0
second_range = 0
third_range = 0
fourth_range = 0
fifth_range = 0
invalid_numbers = 0

for i in range(moves):
    number = int(input())

    if 0 <= number <= 9:
        points += number * 0.2
        first_range += 1
    elif 10 <= number <= 19:
        points += number * 0.3
        second_range += 1
    elif 20 <= number <= 29:
        points += number * 0.4
        third_range += 1
    elif 30 <= number <= 39:
        points += 50
        fourth_range += 1
    elif 40 <= number <= 50:
        points += 100
        fifth_range += 1
    else:
        invalid_numbers += 1
        points /= 2

print(f"{points:.2f}")
print(f"From 0 to 9: {first_range / moves * 100:.2f}%")
print(f"From 10 to 19: {second_range / moves * 100:.2f}%")
print(f"From 20 to 29: {third_range / moves * 100:.2f}%")
print(f"From 30 to 39: {fourth_range / moves * 100:.2f}%")
print(f"From 40 to 50: {fifth_range / moves * 100:.2f}%")
print(f"Invalid numbers: {invalid_numbers / moves * 100:.2f}%")