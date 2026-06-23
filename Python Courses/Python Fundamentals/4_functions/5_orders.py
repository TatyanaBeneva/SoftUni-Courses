COFFEE_PRICE = 1.50
WATER_PRICE = 1.00
COKE_PRICE = 1.40
SNACKS_PRICE = 2.00

def get_price(type_of_product: str) -> float:
    if type_of_product == 'coffee':
        return COFFEE_PRICE
    elif type_of_product == 'water':
        return WATER_PRICE
    elif type_of_product == 'snacks':
        return SNACKS_PRICE
    elif type_of_product == 'coke':
        return COKE_PRICE

    return 0.0

def total_price(price: float, product_quantity: int):
         return price * product_quantity

product = input()
quantity = int(input())

current_price = get_price(product)
result = total_price(current_price, quantity)
print(f"{result:.2f}")