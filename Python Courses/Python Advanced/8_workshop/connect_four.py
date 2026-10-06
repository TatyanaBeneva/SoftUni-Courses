def main():
    player_count = choose_player_count()
    players = [str(number) for number in range(1, player_count + 1)]

    board = create_board()
    turn = 0
    print_board(board)

    while True:
        current_player = players[turn % player_count]
        player_col = choose_column(current_player)

        if player_col is None:
            continue

        col_index = player_col - 1
        row_index = place_player_on_board(board, col_index, current_player)

        if row_index is None:
            print("This column is full. Choose another column.")
            continue

        if check_for_winner(board, current_player):
            print(f"The winner is player {current_player}")
            break

        if is_board_full(board):
            print(f"Thank you for playing! No winner this time.")
            break

        turn += 1


def create_board():
    return [["0" for _ in range(7)] for _ in range(6)]

def print_board(board):
    for row in board:
        print(f"[ {', '.join(row)} ]")

def choose_player_count():
    while True:
        try:
            player_count = int(input("Enter the number of players (2-4): "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if 2 <= player_count <= 4:
            return player_count

        print("Please enter a number between 2 and 4.")

def choose_column(current_player):
    try:
        player_col = int(input(f"Player {current_player}, please choose a column: "))
    except ValueError:
        print("Please enter a valid number between 1 and 7")
        return None

    if not (1 <= player_col <= 7):
        print("Please enter a valid number between 1 and 7")
        return None

    return player_col

def place_player_on_board(board, col_index, current_player):
    row_index = 5

    while row_index >= 0:
        if board[row_index][col_index] == "0":
            board[row_index][col_index] = current_player
            print_board(board)
            return row_index

        row_index -= 1

    return None

def is_board_full(board):
    for row in board:
        if "0" in row:
            return False

    return True

def check_horizontal(board, current_player):
    for row in range(6):
        for col in range(4):
            if (
                board[row][col] == current_player
                and board[row][col+1] == current_player
                and board[row][col+2] == current_player
                and board[row][col+3] == current_player
            ):
                return True

    return False

def check_vertical(board, current_player):
    for col in range(7):
        for row in range(3):
            if (
                board[row][col] == current_player
                and board[row+1][col] == current_player
                and board[row+2][col] == current_player
                and board[row+3][col] == current_player
            ):
                return True

    return False

def check_diagonal(board, current_player):
    # Checking the primary diagonal for winner
    for row in range(3):
        for col in range(4):
            if (
                    board[row][col] == current_player
                    and board[row + 1][col + 1] == current_player
                    and board[row + 2][col + 2] == current_player
                    and board[row + 3][col + 3] == current_player
            ):
                return True

    # Checking the secondary diagonal for winner
    for row in range(3):
        for col in range(3, 7):
            if (
                    board[row][col] == current_player
                    and board[row + 1][col - 1] == current_player
                    and board[row + 2][col - 2] == current_player
                    and board[row + 3][col - 3] == current_player
            ):
                return True

    return False


def check_for_winner(board, current_player):
    return (
        check_horizontal(board, current_player)
        or check_vertical(board, current_player)
        or check_diagonal(board, current_player)
    )


if __name__ == "__main__":
    main()