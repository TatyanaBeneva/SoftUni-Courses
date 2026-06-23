from math import floor, ceil

MAGNOLIAS_PRICE = 3.25
HYACINTHS_PRICE = 4
ROSES_PRICE = 3.5
CACTI_PRICE = 8
TAX_PERCENT = 0.05

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cacti_count = int(input())
gift_price = float(input())

total_sum = magnolias_count * MAGNOLIAS_PRICE + hyacinths_count * HYACINTHS_PRICE + roses_count * ROSES_PRICE + cacti_count * CACTI_PRICE
total_profit = total_sum - (total_sum * TAX_PERCENT)

if total_profit >= gift_price:
    print(f"She is left with {floor(total_profit - gift_price)} leva." )
else:
    print(f"She will have to borrow {ceil(gift_price - total_profit)} leva.")