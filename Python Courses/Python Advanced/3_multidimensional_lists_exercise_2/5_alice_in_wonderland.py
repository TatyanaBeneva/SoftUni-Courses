n = int(input())
field = [input().split() for _ in range(n)]

alice_row = alice_col = 0
tea_bags = 0

# Find Alice
for row in range(n):
    for col in range(n):
        if field[row][col] == "A":
            alice_row, alice_col = row, col
            break

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

# Alice's starting position is part of her path
field[alice_row][alice_col] = "*"

while tea_bags < 10:
    command = input()

    row_step, col_step = directions[command]

    alice_row += row_step
    alice_col += col_step

    # Alice leaves the territory
    if not (0 <= alice_row < n and 0 <= alice_col < n):
        break

    current_position = field[alice_row][alice_col]

    # Alice falls into the rabbit hole
    if current_position == "R":
        field[alice_row][alice_col] = "*"
        break

    # Alice finds tea
    if current_position not in (".", "*"):
        tea_bags += int(current_position)

    # Mark Alice's path
    field[alice_row][alice_col] = "*"

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in field:
    print(*row)