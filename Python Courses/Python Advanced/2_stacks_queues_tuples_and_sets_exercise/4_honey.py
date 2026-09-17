from collections import deque

working_bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0
}

while working_bees and nectar:
    curr_nectar = nectar.pop()

    if curr_nectar >= working_bees[0]:
        curr_bee = working_bees.popleft()
        curr_symbol = symbols.popleft()
        total_honey += abs(operators[curr_symbol](curr_bee, curr_nectar))


print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left: {', '.join(map(str, working_bees))}")

if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")