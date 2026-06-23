rows = int(input())

board = []

for _ in range(rows):
    board.append(input().split())

largest_count = 0

for row in range(len(board)):
    for col in range(len(board[row])):

        if board[row][col] != ".":
            continue

        rows_to_check = [row]
        cols_to_check = [col]

        current_count = 0

        while rows_to_check:
            current_row = rows_to_check.pop()
            current_col = cols_to_check.pop()

            if board[current_row][current_col] != ".":
                continue

            board[current_row][current_col] = "-"
            current_count += 1

            # Up
            if (
                current_row > 0
                and board[current_row - 1][current_col] == "."
            ):
                rows_to_check.append(current_row - 1)
                cols_to_check.append(current_col)

            # Down
            if (
                current_row < len(board) - 1
                and board[current_row + 1][current_col] == "."
            ):
                rows_to_check.append(current_row + 1)
                cols_to_check.append(current_col)

            # Left
            if (
                current_col > 0
                and board[current_row][current_col - 1] == "."
            ):
                rows_to_check.append(current_row)
                cols_to_check.append(current_col - 1)

            # Right
            if (
                current_col < len(board[current_row]) - 1
                and board[current_row][current_col + 1] == "."
            ):
                rows_to_check.append(current_row)
                cols_to_check.append(current_col + 1)

        if current_count > largest_count:
            largest_count = current_count

print(largest_count)