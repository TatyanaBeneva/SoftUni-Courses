rows, cols = [int(el) for el in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

max_sum = float("-inf")
max_row = 0
max_col = 0

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        row_1_col_1 = matrix[row_index][col_index]
        row_1_col_2 = matrix[row_index][col_index + 1]
        row_1_col_3 = matrix[row_index][col_index + 2]

        row_2_col_1 = matrix[row_index + 1][col_index]
        row_2_col_2 = matrix[row_index + 1][col_index + 1]
        row_2_col_3 = matrix[row_index + 1][col_index + 2]

        row_3_col_1 = matrix[row_index + 2][col_index]
        row_3_col_2 = matrix[row_index + 2][col_index + 1]
        row_3_col_3 = matrix[row_index + 2][col_index + 2]

        current_sum = (
            row_1_col_1 + row_1_col_2 + row_1_col_3 +
            row_2_col_1 + row_2_col_2 + row_2_col_3 +
            row_3_col_1 + row_3_col_2 + row_3_col_3
        )

        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row_index
            max_col = col_index

print(f"Sum = {max_sum}")

for row in range(max_row, max_row + 3):
    print(*matrix[row][max_col:max_col + 3])