from math import floor, ceil

tennis_rock_price = float(input())
tennis_rock_count = int(input())
snickers_count = int(input())

snickers_price = tennis_rock_price / 6
tennis_rock_sum = tennis_rock_count * tennis_rock_price
snickers_sum = snickers_count * snickers_price
other_expenses = (tennis_rock_sum + snickers_sum) * 0.2
total_sum = tennis_rock_sum + snickers_sum + other_expenses

tennis_player_pay_sum = total_sum / 8
sponsors_pay_sum = total_sum - tennis_player_pay_sum

print(f"Price to be paid by Djokovic {floor(tennis_player_pay_sum)}")
print(f"Price to be paid by sponsors {ceil(sponsors_pay_sum)}")