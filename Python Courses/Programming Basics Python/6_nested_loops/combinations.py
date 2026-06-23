n = int(input())
iterations = 0

for num_1 in range(n + 1):
    for num_2 in range(n + 1):
        for num_3 in range(n + 1):
            result = num_1 + num_2 + num_3

            if result == n:
                iterations += 1
                break

print(iterations)