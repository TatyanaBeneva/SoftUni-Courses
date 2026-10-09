import tkinter as tk


from connect_four import (
    create_board,
    place_player_on_board,
    check_for_winner,
    is_board_full,
)

ROWS = 6
COLS = 7
CELL_SIZE = 70
PLAYER_COLORS = {"1": "#e65353", "2": "#f4c542", "3": "#4eb979", "4": "#b985de"}


def create_ui(root):
    # This list stores the actual game. The Canvas below only displays it.
    board = create_board()
    turn = 0
    game_over = False

    # Tkinter variables connect Python values to widgets on the screen.
    player_count = tk.IntVar(value=2)
    status = tk.StringVar(value="Player 1's turn")

    def draw_board():
        """Redraw the circles using the current values in the board list."""
        canvas.delete("all")
        for row in range(ROWS):
            for col in range(COLS):
                player = board[row][col]
                color = PLAYER_COLORS.get(player, "white")

                # Canvas coordinates start at the top-left corner (0, 0).
                # An oval inside a square bounding box becomes a circle.
                left = col * CELL_SIZE + 7
                top = row * CELL_SIZE + 7
                canvas.create_oval(
                    left, top,
                    left + CELL_SIZE - 14, top + CELL_SIZE - 14,
                    fill=color, outline="",
                )
                if player != "0":
                    canvas.create_text(
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2,
                        text=player, font=("Arial", 16, "bold"),
                    )

    def play_column(col):
        """A button click plays one turn instead of asking for console input."""
        nonlocal turn, game_over
        if game_over:
            return

        current_player = str(turn % player_count.get() + 1)
        # The existing function drops the piece into the lowest free row.
        # It also prints the board in the console, just like the original game.
        row = place_player_on_board(board, col, current_player)
        if row is None:
            status.set(f"Column full. Player {current_player}, choose another.")
            return

        draw_board()
        if check_for_winner(board, current_player):
            status.set(f"Player {current_player} wins!")
            game_over = True
        elif is_board_full(board):
            status.set("Draw! The board is full.")
            game_over = True
        else:
            turn += 1
            next_player = str(turn % player_count.get() + 1)
            status.set(f"Player {next_player}'s turn")

        if game_over:
            for button in column_buttons:
                button.config(state=tk.DISABLED)

    def new_game(selected_count=None):
        # nonlocal lets this function replace variables from create_ui().
        # OptionMenu passes the selected count; the restart button passes nothing.
        nonlocal board, turn, game_over
        board = create_board()
        turn = 0
        game_over = False
        status.set("Player 1's turn")
        for button in column_buttons:
            button.config(state=tk.NORMAL)
        draw_board()

    # A Frame groups widgets. pack() arranges these groups vertically.
    controls = tk.Frame(root)
    controls.pack(pady=10)
    tk.Label(controls, text="Players:").pack(side=tk.LEFT)
    # Changing the number of players starts a fresh game.
    tk.OptionMenu(controls, player_count, 2, 3, 4, command=new_game).pack(side=tk.LEFT)
    # Pass the function itself to command, without (). Tkinter calls it on click.
    tk.Button(controls, text="New game", command=new_game).pack(side=tk.LEFT, padx=15)

    tk.Label(root, textvariable=status, font=("Arial", 14)).pack(pady=(0, 10))

    board_frame = tk.Frame(root)
    board_frame.pack(padx=12, pady=(0, 12))
    column_buttons = []
    for col in range(COLS):
        # col=col remembers this button's column, so each button plays a
        # different column. Without it, all buttons would use the last column.
        button = tk.Button(
            board_frame, text=str(col + 1),
            command=lambda col=col: play_column(col),
        )
        # grid() places widgets in rows and columns within this Frame.
        button.grid(row=0, column=col, sticky="ew", padx=3, pady=(0, 6))
        board_frame.columnconfigure(col, minsize=CELL_SIZE, weight=1)
        column_buttons.append(button)

    # Canvas is a drawing area. One canvas spans all seven button columns.
    canvas = tk.Canvas(
        board_frame, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE,
        bg="#2666a5", highlightthickness=0,
    )
    canvas.grid(row=1, column=0, columnspan=COLS)
    draw_board()

def start_game():
    # Tk() creates the main application window.
    root = tk.Tk()
    root.title("Connect Four")
    root.resizable(False, False)

    create_ui(root)

    # mainloop() keeps the window open and waits for clicks and other events.
    # We do not need a while loop: each click calls a function above.
    root.mainloop()


# Run the window only when this file is started directly.
if __name__ == "__main__":
    start_game()
