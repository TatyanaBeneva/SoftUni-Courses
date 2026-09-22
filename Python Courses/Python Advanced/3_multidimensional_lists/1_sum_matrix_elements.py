n_rows, n_cols = [int(el) for el in input().split(", ")]

matrix = []
total_sum = 0

for _ in range(n_rows):
    data = [int(el) for el in input().split(", ")]
    matrix.append(data)
    total_sum += sum(data)

print(total_sum)
print(matrix)
