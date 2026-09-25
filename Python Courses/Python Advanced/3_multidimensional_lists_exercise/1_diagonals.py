n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(el) for el in input().split(", ")])

primary_diagonal_sum = 0
primary_diagonal = []
secondary_diagonal_sum = 0
secondary_diagonal = []

for i in range(n):
    primary_diagonal_sum += matrix[i][i]
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal_sum += matrix[i][n - i - 1]
    secondary_diagonal.append(matrix[i][n - i - 1])

print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {primary_diagonal_sum}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {secondary_diagonal_sum}')