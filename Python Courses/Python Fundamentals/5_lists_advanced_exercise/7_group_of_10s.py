from math import ceil

numbers = list(map(int, input().split(", ")))
rounds = ceil(max(numbers) / 10)
prev_boundry = 0
next_boundry = 10

for _ in range(rounds):
    grouped_list = list(filter(lambda x: prev_boundry < x <= next_boundry , numbers))
    print(f"Group of {next_boundry}'s: {grouped_list}")

    prev_boundry = next_boundry
    next_boundry += 10