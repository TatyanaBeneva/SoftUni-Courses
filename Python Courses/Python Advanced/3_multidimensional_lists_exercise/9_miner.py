size = int(input())
commands = input().split()

field = []

miner_row = 0
miner_col = 0
coal_count = 0

for row in range(size):
    current_row = input().split()
    field.append(current_row)

    for col in range(size):
        if current_row[col] == "s":
            miner_row = row
            miner_col = col

        elif current_row[col] == "c":
            coal_count += 1


directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

game_over = False
all_coal_collected = False

for command in commands:
    row_change, col_change = directions[command]

    new_row = miner_row + row_change
    new_col = miner_col + col_change

    # Ignore command if miner would leave the field
    if not (0 <= new_row < size and 0 <= new_col < size):
        continue

    miner_row = new_row
    miner_col = new_col

    # Coal
    if field[miner_row][miner_col] == "c":
        coal_count -= 1
        field[miner_row][miner_col] = "*"

        if coal_count == 0:
            all_coal_collected = True
            break

    # End
    elif field[miner_row][miner_col] == "e":
        game_over = True
        break


if all_coal_collected:
    print(f"You collected all coal! ({miner_row}, {miner_col})")

elif game_over:
    print(f"Game over! ({miner_row}, {miner_col})")

else:
    print(f"{coal_count} pieces of coal left. ({miner_row}, {miner_col})")