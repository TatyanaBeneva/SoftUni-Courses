rows, cols = map(int, input().split())

matrix = []

for _ in range(rows):
    matrix.append(input().split())

while True:
    command = input()

    if command == "END":
        break

    data = command.split()

    if len(data) != 5 or data[0] != "swap":
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = map(int, data[1:])

    valid_rows = 0 <= row1 < rows and 0 <= row2 < rows
    valid_cols = 0 <= col1 < cols and 0 <= col2 < cols

    if not valid_rows or not valid_cols:
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = \
        matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(" ".join(row))