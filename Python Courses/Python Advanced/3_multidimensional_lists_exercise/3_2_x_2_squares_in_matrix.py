rows, cols = [int(el) for el in input().split()]
matrix = []

for _ in range(rows):
    data = input().split()
    matrix.append(data)

count = 0

for row_index in range(rows-1):
    for col_index in range(cols-1):
        current = matrix[row_index][col_index]
        next_el = matrix[row_index][col_index + 1]
        el_below = matrix[row_index + 1][col_index]
        el_diagonal = matrix[row_index + 1][col_index + 1]

        if current == next_el == el_below == el_diagonal:
            count += 1

print(count)