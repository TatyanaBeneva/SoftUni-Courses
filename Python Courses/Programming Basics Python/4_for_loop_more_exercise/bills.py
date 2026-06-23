WATER_EXPENSES = 20
INTERNET_EXPENSES = 15

months = int(input())
water_expenses_sum =  WATER_EXPENSES * months
internet_expenses_sum = INTERNET_EXPENSES * months
energy_expenses_sum = 0.0
other_expenses_sum = 0.0

for i in range(1, months + 1):
    energy_expenses = float(input())
    other_expenses = energy_expenses + WATER_EXPENSES + INTERNET_EXPENSES + ((energy_expenses + WATER_EXPENSES + INTERNET_EXPENSES) * 0.2)
    energy_expenses_sum += energy_expenses
    other_expenses_sum += other_expenses

all_expenses = water_expenses_sum + internet_expenses_sum + energy_expenses_sum + other_expenses_sum

print(f"Electricity: {energy_expenses_sum:.2f} lv")
print(f"Water: {water_expenses_sum:.2f} lv")
print(f"Internet: {internet_expenses_sum:.2f} lv")
print(f"Other: {other_expenses_sum:.2f} lv")
print(f"Average: {all_expenses / months:.2f} lv")
