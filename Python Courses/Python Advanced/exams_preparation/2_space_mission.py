START_UNITS = 100

n = int(input())
matrix = []
space_position = None
planet_b = None
units = START_UNITS

for row_index in range(n):
    row = input().split()
    matrix.append(row)

    if "S" in row:
        space_position = (row_index, row.index("S"))
    if "P" in row:
        planet_b = (row_index, row.index("P"))

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()

    if command not in directions:
        continue

    row, col = space_position
    row_change, col_change = directions[command]

    next_row = row + row_change
    next_col = col + col_change

    if not (0 <= next_row < n and 0 <= next_col < n):
        print("Mission failed! The spaceship was lost in space.")
        matrix[row][col] = "S"
        break

    units -= 5
    destination = matrix[next_row][next_col]
    space_position = (next_row, next_col)

    if matrix[row][col] == "S":
        matrix[row][col] = "."

    if destination == "R":
        if units + 10 > 100:
            units = 100
        else:
            units += 10

    if destination == "M":
        units -= 5
        matrix[next_row][next_col] = "."

    if destination == "P":
        print(f"Mission accomplished! The spaceship reached Planet B with {units} resources left.")
        break

    if units < 5:
        print("Mission failed! The spaceship was stranded in space.")
        matrix[next_row][next_col] = "S"
        break

for row in matrix:
    print(*row)