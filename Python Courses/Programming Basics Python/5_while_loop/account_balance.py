new_input = input()
total_sum = 0.0

while new_input != "NoMoreMoney":
    amount = float(new_input)

    if amount < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {amount:.2f}")
    total_sum += amount
    new_input = input()

print(f"Total: {total_sum:.2f}")