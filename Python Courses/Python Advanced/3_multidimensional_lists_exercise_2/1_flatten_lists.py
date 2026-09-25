matrix = [i.split() for i in input().split("|")]

result = []

for row in reversed(matrix):
    result.extend(row)

print(*result)