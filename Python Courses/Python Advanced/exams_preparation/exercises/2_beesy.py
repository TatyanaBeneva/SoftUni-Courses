BEE_ENERGY = 15
NEEDED_NECTAR = 30

n = int(input())
matrix  = []
bee_position = None
energy = BEE_ENERGY
total_nectar = 0
recharge_used = False
for row_index in range(n):
    row = list(input())
    matrix.append(row)

    if "B" in row:
        bee_position = (row_index, row.index("B"))

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

    row, col = bee_position
    row_change, col_change = directions[command]

    next_row = row + row_change
    next_col = col + col_change


    if not (0 <= next_row < n and 0 <= next_col < n):
        if command == "up":
            next_row = n-1
        elif command == "down":
            next_row = 0
        elif command == "left":
            next_col = n-1
        elif command == "right":
            next_col = 0

    energy -= 1
    destination = matrix[next_row][next_col]
    bee_position = (next_row, next_col)

    if matrix[row][col] == "B":
        matrix[row][col] = "-"

    if destination.isdigit():
        total_nectar += int(destination)
        matrix[next_row][next_col] = "-"

    if destination == "H":
        if total_nectar >= NEEDED_NECTAR:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")

        break

    if energy <= 0 and total_nectar < NEEDED_NECTAR:
        print("This is the end! Beesy ran out of energy.")
        break

    if energy <= 0 and total_nectar >= NEEDED_NECTAR:
        if recharge_used or total_nectar == NEEDED_NECTAR:
            print("This is the end! Beesy ran out of energy.")
            break

        recharge_used = True
        energy += total_nectar - NEEDED_NECTAR
        total_nectar = NEEDED_NECTAR

row, col = bee_position
matrix[row][col] = "B"

for row in matrix:
    print("".join(row))
