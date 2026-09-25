n = int(input())
board = [input().split() for _ in range(n)]

bunny_row = bunny_col = 0

for row in range(n):
    for col in range(n):
        if board[row][col] == "B":
            bunny_row, bunny_col = row, col
            break

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

best_direction = ""
best_path = []
max_eggs = float("-inf")

for direction, (row_step, col_step) in directions.items():
    row = bunny_row + row_step
    col = bunny_col + col_step

    # Bunny cannot move in this direction
    if not (0 <= row < n and 0 <= col < n):
        continue

    current_eggs = 0
    path = []

    while 0 <= row < n and 0 <= col < n:
        if board[row][col] == "X":
            break

        current_eggs += int(board[row][col])
        path.append([row, col])

        row += row_step
        col += col_step

    if current_eggs > max_eggs:
        max_eggs = current_eggs
        best_direction = direction
        best_path = path

print(best_direction)

for position in best_path:
    print(position)

print(max_eggs)