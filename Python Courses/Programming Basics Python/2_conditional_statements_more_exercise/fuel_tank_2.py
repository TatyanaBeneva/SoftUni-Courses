GASOLINE_PRICE = 2.22
DIESEL_PRICE = 2.33
GAS_PRICE = 0.93
GASOLINE_PRICE_WITH_DISCOUNT = GASOLINE_PRICE - 0.18
DIESEL_PRICE_WITH_DISCOUNT = DIESEL_PRICE - 0.12
GAS_PRICE_WITH_DISCOUNT = GAS_PRICE - 0.08

fuel_type = input()
fuel_litters = float(input())
is_card_discount = input()

fuel_sum = 0

if is_card_discount == "Yes":
    if fuel_type == "Gasoline":
        fuel_sum = GASOLINE_PRICE_WITH_DISCOUNT * fuel_litters
    elif fuel_type == "Diesel":
        fuel_sum = DIESEL_PRICE_WITH_DISCOUNT * fuel_litters
    elif fuel_type == "Gas":
        fuel_sum = GAS_PRICE_WITH_DISCOUNT * fuel_litters
elif is_card_discount == "No":
    if fuel_type == "Gasoline":
        fuel_sum = GASOLINE_PRICE * fuel_litters
    elif fuel_type == "Diesel":
        fuel_sum = DIESEL_PRICE * fuel_litters
    elif fuel_type == "Gas":
        fuel_sum = GAS_PRICE * fuel_litters

if 20 <= fuel_litters <= 25:
    fuel_sum -= fuel_sum * 0.08
elif fuel_litters > 25:
    fuel_sum -= fuel_sum * 0.1

print(f"{fuel_sum:.2f} lv.")