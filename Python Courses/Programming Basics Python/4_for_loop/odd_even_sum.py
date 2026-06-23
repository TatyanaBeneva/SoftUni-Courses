n = int(input())
sum_odd = 0
sum_even = 0

for index in range(n):
    new_number = int(input())

    if index % 2 == 0:
        sum_even += new_number
    else:
        sum_odd += new_number

if sum_odd == sum_even:
    print("Yes")
    print(f"Sum = {sum_even}")
else:
    print("No")
    print(f"Diff = {abs(sum_even - sum_odd)}")