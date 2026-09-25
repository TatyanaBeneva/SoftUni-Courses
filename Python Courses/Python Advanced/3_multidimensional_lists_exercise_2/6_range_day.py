field = [input().split() for _ in range(5)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

player_row = player_col = 0
targets = 0

# Find player and count targets
for row in range(5):
    for col in range(5):
        if field[row][col] == "A":
            player_row, player_col = row, col
        elif field[row][col] == "x":
            targets += 1

initial_targets = targets
hit_targets = []

commands_count = int(input())

for _ in range(commands_count):
    command = input().split()

    action = command[0]
    direction = command[1]

    row_step, col_step = directions[direction]

    if action == "move":
        steps = int(command[2])

        new_row = player_row + row_step * steps
        new_col = player_col + col_step * steps

        if (
            0 <= new_row < 5
            and 0 <= new_col < 5
            and field[new_row][new_col] == "."
        ):
            field[player_row][player_col] = "."
            player_row, player_col = new_row, new_col
            field[player_row][player_col] = "A"

    elif action == "shoot":
        shot_row = player_row + row_step
        shot_col = player_col + col_step

        while 0 <= shot_row < 5 and 0 <= shot_col < 5:
            if field[shot_row][shot_col] == "x":
                field[shot_row][shot_col] = "."
                hit_targets.append([shot_row, shot_col])
                targets -= 1
                break

            shot_row += row_step
            shot_col += col_step

    if targets == 0:
        break

if targets == 0:
    print(f"Training completed! All {initial_targets} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")

for target in hit_targets:
    print(target)