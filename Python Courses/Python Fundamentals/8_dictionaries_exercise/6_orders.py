products = {}

while True:
    data = input()

    if data == "buy":
        break

    product, price, quantity = data.split(" ")
    price = float(price)
    quantity = int(quantity)

    if product not in products:
        products[product] = {"price": price, "quantity": quantity}
    else:
        products[product]["price"] = price
        products[product]["quantity"] += quantity

for product, items in products.items():
    total_price = items['price'] * items['quantity']
    print(f"{product} -> {total_price:.2f}")