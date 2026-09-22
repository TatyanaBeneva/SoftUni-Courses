rows, cols = map(int, input().split())

lair = []

player_row = 0
player_col = 0

for row in range(rows):
    current_row = list(input())
    lair.append(current_row)

    for col in range(cols):
        if current_row[col] == "P":
            player_row = row
            player_col = col

commands = input()

directions = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}


def spread_bunnies():
    bunnies = []

    # Find all CURRENT bunnies first
    for row in range(rows):
        for col in range(cols):
            if lair[row][col] == "B":
                bunnies.append((row, col))

    bunny_directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    # Spread each bunny
    for bunny_row, bunny_col in bunnies:
        for row_change, col_change in bunny_directions:
            new_row = bunny_row + row_change
            new_col = bunny_col + col_change

            if 0 <= new_row < rows and 0 <= new_col < cols:
                lair[new_row][new_col] = "B"


won = False
dead = False

final_row = player_row
final_col = player_col

for command in commands:
    row_change, col_change = directions[command]

    new_row = player_row + row_change
    new_col = player_col + col_change

    # Remove player from the old position
    lair[player_row][player_col] = "."

    # Player leaves the lair
    if not (0 <= new_row < rows and 0 <= new_col < cols):
        final_row = player_row
        final_col = player_col
        won = True

        spread_bunnies()
        break

    # Player moves
    player_row = new_row
    player_col = new_col

    # Player steps directly on a bunny
    if lair[player_row][player_col] == "B":
        final_row = player_row
        final_col = player_col
        dead = True

        spread_bunnies()
        break

    # Put player on the new position
    lair[player_row][player_col] = "P"

    # Bunnies spread after player's move
    spread_bunnies()

    # Check if a bunny reached the player
    if lair[player_row][player_col] == "B":
        final_row = player_row
        final_col = player_col
        dead = True
        break


for row in lair:
    print("".join(row))

if won:
    print(f"won: {final_row} {final_col}")
else:
    print(f"dead: {final_row} {final_col}")