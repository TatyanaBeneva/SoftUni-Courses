PUZZLE_PRICE = 2.6
TALKING_DOLL_PRICE = 3
BEAR_PRICE = 4.1
MINION_PRICE = 8.2
TRUCK_PRICE = 2

travel_price = float(input())
puzzle_count = int(input())
talking_doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

total_sum = puzzle_count * PUZZLE_PRICE + talking_doll_count * TALKING_DOLL_PRICE + bear_count * BEAR_PRICE + minion_count * MINION_PRICE + truck_count * TRUCK_PRICE
total_count = puzzle_count + talking_doll_count + bear_count + minion_count + truck_count

if total_count >= 50:
    total_sum = total_sum - (total_sum * 0.25)

total_sum_after_rent = total_sum - (total_sum * 0.1)

if total_sum_after_rent >= travel_price:
    print(f'Yes! {(total_sum_after_rent - travel_price):.2f} lv left.')
else:
    print(f'Not enough money! {(travel_price - total_sum_after_rent):.2f} lv needed.')