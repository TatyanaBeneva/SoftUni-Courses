budget = float(input())
flour_kilo_price = float(input())
pack_of_eggs_price = flour_kilo_price * 0.75
liter_of_milk_price = flour_kilo_price + (flour_kilo_price * 0.25)
price_for_one_loaves = flour_kilo_price + pack_of_eggs_price + (liter_of_milk_price * 0.25)
received_colored_eggs = 0
made_loaves = 0
counter = 1

while budget > 0:
    if budget - price_for_one_loaves > 0:
        budget -= price_for_one_loaves
        made_loaves += 1
        received_colored_eggs += 3

        if counter % 3 == 0:
            received_colored_eggs -= made_loaves - 2

        counter += 1
    else:
        break

print(f"You made {made_loaves} loaves of Easter bread! Now you have {received_colored_eggs} eggs and {budget:.2f}BGN left.")