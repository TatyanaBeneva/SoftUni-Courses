n = int(input())
sum_number = 0

for i in range(n):
    number = int(input())
    sum_number += number

print(f"{sum_number / n:.2f}")
