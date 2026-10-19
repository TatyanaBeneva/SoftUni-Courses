STAR = "*"
GHOST = "G"
PACMAN = "P"
FREEZER = "F"
EMPTY_POSITION = "-"
INITIAL_HEALTH = 100

def main():
    n = int(input())
    matrix = []
    pacman_position = None
    stars_count = 0
    health = INITIAL_HEALTH
    has_freezer = False

    for row_index in range(n):
        row = list(input())
        matrix.append(row)

        if PACMAN in row:
            col_index = row.index(PACMAN)
            pacman_position = (row_index, col_index)
            row[col_index] = EMPTY_POSITION

        stars_count += row.count(STAR)

    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    while health > 0 and stars_count > 0:
        command = input()

        if command == "end":
            break

        if command not in directions:
            continue

        row, col = pacman_position
        row_change, col_change = directions[command]

        next_row = (row + row_change) % n
        next_col = (col + col_change) % n

        destination = matrix[next_row][next_col]
        pacman_position = (next_row, next_col)
        matrix[next_row][next_col] = EMPTY_POSITION

        if destination == EMPTY_POSITION:
            continue

        if destination == STAR:
            stars_count -= 1
        elif destination == GHOST:
            if has_freezer:
                has_freezer = False
            else:
                health -= 50
        elif destination == FREEZER:
            has_freezer = True

    row, col = pacman_position
    matrix[row][col] = PACMAN

    app_result(health, stars_count, matrix, row, col)


def app_result(health, stars_count, matrix, row, col):
    if health <= 0:
        print(f"Game over! Pacman last coordinates [{row},{col}]")
    elif stars_count == 0:
        print("Pacman wins! All the stars are collected.")
    else:
        print("Pacman failed to collect all the stars.")

    print(f"Health: {health}")

    if stars_count > 0:
        print(f"Uncollected stars: {stars_count}")

    for row in matrix:
        print("".join(row))

if __name__ == "__main__":
    main()