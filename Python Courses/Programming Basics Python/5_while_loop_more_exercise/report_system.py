needed_sum = int(input())

collected_sum = 0
cash_sum = 0
card_sum = 0
cash_payments = 0
card_payments = 0
transaction = 0

while collected_sum < needed_sum:
    command = input()

    if command == "End":
        break

    price = int(command)
    transaction += 1

    is_cash_payment = transaction % 2 != 0

    if is_cash_payment:
        if price > 100:
            print("Error in transaction!")
            continue

        cash_sum += price
        cash_payments += 1
    else:
        if price < 10:
            print("Error in transaction!")
            continue

        card_sum += price
        card_payments += 1

    collected_sum += price
    print("Product sold!")

if collected_sum >= needed_sum:
    print(f"Average CS: {cash_sum / cash_payments:.2f}")
    print(f"Average CC: {card_sum / card_payments:.2f}")
else:
    print("Failed to collect required money for charity.")