from collections import deque

working_bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0

while working_bees and nectar:
    bee = working_bees[0]
    current_nectar = nectar[-1]

    if current_nectar < bee:
        nectar.pop()
        continue

    symbol = symbols.popleft()

    if symbol == "/" and current_nectar == 0:
        working_bees.popleft()
        nectar.pop()
        continue

    match symbol:
        case "+":
            result = bee + current_nectar
        case "-":
            result = bee - current_nectar
        case "*":
            result = bee * current_nectar
        case "/":
            result = bee / current_nectar

    total_honey += abs(result)

    working_bees.popleft()
    nectar.pop()

print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left: {', '.join(map(str, working_bees))}")

if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")