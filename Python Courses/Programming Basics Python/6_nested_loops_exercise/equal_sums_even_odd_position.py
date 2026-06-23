n1 = int(input())
n2 = int(input())

for num in range(n1, n2 + 1):
    even_sum = 0
    odd_sum = 0

    for index in range(6):
        if index % 2 == 0:
            even_sum += int(str(num)[index])
        else:
            odd_sum += int(str(num)[index])

    if even_sum == odd_sum and even_sum != 0:
        print(f"{num}", end=" ")