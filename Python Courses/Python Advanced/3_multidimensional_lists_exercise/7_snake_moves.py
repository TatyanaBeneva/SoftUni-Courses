rows, cols = map(int, input().split())
snake = input()

index = 0

for row in range(rows):
    current_row = [""] * cols

    for col in range(cols):
        position = col if row % 2 == 0 else cols - 1 - col

        current_row[position] = snake[index % len(snake)]
        index += 1

    print("".join(current_row))