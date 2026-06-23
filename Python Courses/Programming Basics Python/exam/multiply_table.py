n = int(input())

n1 = int(str(n)[0])
n2 = int(str(n)[1])
n3 = int(str(n)[2])

for num1 in range(1, n3 + 1):
    for num2 in range(1, n2 + 1):
        for num3 in range(1, n1 + 1):
            total_sum = num1 * num2 * num3

            print(f"{num1} * {num2} * {num3} = {total_sum};")