presents = int(input())
n = int(input())

neighborhood = [input().split() for _ in range(n)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

santa_row = santa_col = 0
nice_kids = 0

# Find Santa and count the nice kids
for row in range(n):
    for col in range(n):
        if neighborhood[row][col] == "S":
            santa_row, santa_col = row, col
        elif neighborhood[row][col] == "V":
            nice_kids += 1

nice_kids_left = nice_kids

while presents > 0:
    command = input()

    if command == "Christmas morning":
        break

    row_step, col_step = directions[command]

    new_row = santa_row + row_step
    new_col = santa_col + col_step

    # Remove Santa from his old position
    neighborhood[santa_row][santa_col] = "-"

    current_position = neighborhood[new_row][new_col]

    # Nice kid
    if current_position == "V":
        presents -= 1
        nice_kids_left -= 1

    # Cookie
    elif current_position == "C":
        for row_step, col_step in directions.values():
            kid_row = new_row + row_step
            kid_col = new_col + col_step

            if 0 <= kid_row < n and 0 <= kid_col < n:
                if neighborhood[kid_row][kid_col] in ("V", "X"):
                    if neighborhood[kid_row][kid_col] == "V":
                        nice_kids_left -= 1

                    neighborhood[kid_row][kid_col] = "-"
                    presents -= 1

                    if presents == 0:
                        break

    santa_row, santa_col = new_row, new_col
    neighborhood[santa_row][santa_col] = "S"

if presents == 0 and nice_kids_left > 0:
    print("Santa ran out of presents!")

for row in neighborhood:
    print(*row)

if nice_kids_left == 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")