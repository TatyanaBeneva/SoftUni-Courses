n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(el) for el in input().split(", ")])

primary_diagonal_sum = 0
primary_diagonal = []
secondary_diagonal_sum = 0
secondary_diagonal = []

for index in range(n):
    el = matrix[index][index]
    primary_diagonal_sum += el
    primary_diagonal.append(el)

for i in range(n):
    el = matrix[i][n - i - 1]
    secondary_diagonal_sum += el
    secondary_diagonal.append(el)

print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {primary_diagonal_sum}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {secondary_diagonal_sum}')