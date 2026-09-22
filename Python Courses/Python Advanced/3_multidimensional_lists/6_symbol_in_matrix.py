n = int(input())

matrix = []

for _ in range(n):
    data = list(input())
    matrix.append(data)

searched_symbol = input()
position = None

for index_row in range(n):
    for index_column in range(n):
        if matrix[index_row][index_column] == searched_symbol:
            position = (index_row, index_column)
            print(position)
            exit()

print(f"{searched_symbol} does not occur in the matrix")