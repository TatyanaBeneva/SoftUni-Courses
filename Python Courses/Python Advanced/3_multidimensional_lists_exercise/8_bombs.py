size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

for bomb in bombs:
    row, col = [int(x) for x in bomb.split(",")]

    bomb_value = matrix[row][col]

    if bomb_value <= 0:
        continue

    for current_row in range(row - 1, row + 2):
        for current_col in range(col - 1, col + 2):

            if current_row == row and current_col == col:
                continue

            if 0 <= current_row < size and 0 <= current_col < size:
                if matrix[current_row][current_col] > 0:
                    matrix[current_row][current_col] -= bomb_value

    matrix[row][col] = 0

alive_cells = 0
alive_sum = 0

for row in matrix:
    for cell in row:
        if cell > 0:
            alive_cells += 1
            alive_sum += cell

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_sum}")

for row in matrix:
    print(*row)