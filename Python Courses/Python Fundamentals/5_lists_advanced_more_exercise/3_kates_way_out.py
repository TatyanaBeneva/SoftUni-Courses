rows_in_maze = int(input())

maze = []
start_row = 0
start_col = 0

for row in range(rows_in_maze):
    current_row = list(input())
    maze.append(current_row)

    if "k" in current_row:
        start_row = row
        start_col = current_row.index("k")


rows_to_check = [start_row]
cols_to_check = [start_col]
moves_to_check = [1]

longest_path = 0
is_out = False

while rows_to_check:
    current_row = rows_to_check.pop()
    current_col = cols_to_check.pop()
    current_moves = moves_to_check.pop()

    if maze[current_row][current_col] == "#":
        continue

    maze[current_row][current_col] = "#"

    if (
        current_row == 0
        or current_row == len(maze) - 1
        or current_col == 0
        or current_col == len(maze[current_row]) - 1
    ):
        is_out = True

        if current_moves > longest_path:
            longest_path = current_moves

    # Up
    if (
        current_row > 0
        and maze[current_row - 1][current_col] == " "
    ):
        rows_to_check.append(current_row - 1)
        cols_to_check.append(current_col)
        moves_to_check.append(current_moves + 1)

    # Down
    if (
        current_row < len(maze) - 1
        and maze[current_row + 1][current_col] == " "
    ):
        rows_to_check.append(current_row + 1)
        cols_to_check.append(current_col)
        moves_to_check.append(current_moves + 1)

    # Left
    if (
        current_col > 0
        and maze[current_row][current_col - 1] == " "
    ):
        rows_to_check.append(current_row)
        cols_to_check.append(current_col - 1)
        moves_to_check.append(current_moves + 1)

    # Right
    if (
        current_col < len(maze[current_row]) - 1
        and maze[current_row][current_col + 1] == " "
    ):
        rows_to_check.append(current_row)
        cols_to_check.append(current_col + 1)
        moves_to_check.append(current_moves + 1)


if is_out:
    print(f"Kate got out in {longest_path} moves")
else:
    print("Kate cannot get out")