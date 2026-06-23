import sys

numbers_count = int(input())
max_num = -sys.maxsize
sum_numbers = 0

for number in range(0, numbers_count):
    n = int(input())

    if n > max_num:
        max_num = n

    sum_numbers += n

sum_numbers -= max_num

if max_num == sum_numbers:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(max_num - sum_numbers)}")