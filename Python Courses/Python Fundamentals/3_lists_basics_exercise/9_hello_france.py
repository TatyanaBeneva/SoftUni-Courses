train_ticket_price = 150
markup = 0.4

items = input().split("|")
budget = float(input())
bought_items_price = []
profit = 0.0

for item in items:
    item_array = item.split("->")
    item_type = item_array[0]
    item_price = float(item_array[1])

    if (item_type == "Clothes" and item_price > 50.00) or\
            (item_type == "Shoes" and item_price > 35.00) or\
            (item_type == "Accessories" and item_price > 20.50):
        continue

    if budget - item_price >= 0:
        budget -= item_price
        new_price = item_price * (1 + markup)
        profit += new_price - item_price
        bought_items_price.append(new_price)

for price in bought_items_price:
    print(f"{price:.2f}", end=" ")

print()

total_sum = budget + sum(bought_items_price)
print(f"Profit: {profit:.2f}")

if total_sum >= train_ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")