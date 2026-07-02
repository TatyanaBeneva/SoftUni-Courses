stock = {}

while True:
    line = input()

    if line == "statistics":
        break

    product, quantity = line.split(": ")

    if product in stock:
        stock[product] += int(quantity)
    else:
        stock[product] = int(quantity)

print("Products in stock:")

for product, quantity in stock.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")