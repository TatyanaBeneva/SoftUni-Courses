n = int(input())

board = [list(input()) for _ in range(n)]

moves = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1),
]

removed_knights = 0

while True:
    max_attacks = 0
    knight_to_remove = None

    for row in range(n):
        for col in range(n):

            if board[row][col] != "K":
                continue

            attacks = 0

            for row_move, col_move in moves:
                new_row = row + row_move
                new_col = col + col_move

                if 0 <= new_row < n and 0 <= new_col < n and board[new_row][new_col] == "K":
                    attacks += 1

            if attacks > max_attacks:
                max_attacks = attacks
                knight_to_remove = (row, col)

    if max_attacks == 0:
        break

    row, col = knight_to_remove
    board[row][col] = "0"
    removed_knights += 1

print(removed_knights)