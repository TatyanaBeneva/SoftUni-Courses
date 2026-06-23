PREMIERE = 12
NORMAL = 7.5
DISCOUNT = 5

screening_type = input()
rows = int(input())
columns = int(input())

cinema_capacity = rows * columns
income = 0

if screening_type == "Premiere":
    income = cinema_capacity * 12
elif screening_type == "Normal":
    income = cinema_capacity * NORMAL
elif screening_type == "Discount":
    income = cinema_capacity * DISCOUNT

print(f"{income:.2f} leva")