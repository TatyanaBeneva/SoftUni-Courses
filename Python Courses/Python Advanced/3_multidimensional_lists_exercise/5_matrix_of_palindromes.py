rows, cols = map(int, input().split())

matrix = []

for row in range(rows):
    current_row = []
    first_char = chr(97 + row)

    for col in range(cols):
        second_char = chr(97 + row + col)

        word = first_char + second_char + first_char
        current_row.append(word)

    matrix.append(current_row)

for row in matrix:
    print(" ".join(row))