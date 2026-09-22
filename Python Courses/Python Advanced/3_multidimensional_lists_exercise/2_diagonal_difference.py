n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(el) for el in input().split()])

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for index in range(n):
    primary_diagonal_sum += matrix[index][index]
    secondary_diagonal_sum += matrix[index][n - index - 1]

difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

print(difference)