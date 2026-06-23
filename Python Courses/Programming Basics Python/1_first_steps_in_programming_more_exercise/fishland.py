MUSSELS_PRICE = 7.50

mackerel_price = float(input())
caca_price = float(input())
bonito_kilos = float(input())
horse_mackerel_kilos = float(input())
mussels_kilos = int(input())

bonito_price = mackerel_price + (mackerel_price * 0.6)
horse_mackerel_price = caca_price + (caca_price * 0.8)

bonito_sum = bonito_price * bonito_kilos
horse_mackerel_sum = horse_mackerel_price * horse_mackerel_kilos
mussels_sum = mussels_kilos * MUSSELS_PRICE

total_sum = bonito_sum + horse_mackerel_sum + mussels_sum

print(f'{total_sum:.2f}')