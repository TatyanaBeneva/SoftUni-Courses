n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]

while True:
    command = input()

    if command == "END":
        break

    action, row, col, value = command.split()

    row = int(row)
    col = int(col)
    value = int(value)

    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[row]):
        print("Invalid coordinates")
        continue

    if action == "Add":
        matrix[row][col] += value

    elif action == "Subtract":
        matrix[row][col] -= value

for row in matrix:
    print(*row)