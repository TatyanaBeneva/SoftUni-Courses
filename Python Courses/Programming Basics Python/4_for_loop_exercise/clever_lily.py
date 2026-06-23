age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

sum_per_year = 10
total_sum = 0

for num in range(1, age + 1):
    if num % 2 == 0:
        total_sum += sum_per_year - 1
        sum_per_year += 10
    else:
        total_sum += toy_price

sum_diff = abs(total_sum - washing_machine_price)

if total_sum >= washing_machine_price:
    print(f"Yes! {sum_diff:.2f}")
else:
    print(f"No! {sum_diff:.2f}")