LOVE_LETTER_PRICE = 0.6
ROSE_PRICE = 7.20
KEYKEEPER_PRICE = 3.6
CARTOON_PRICE = 18.2
LUCKY_SURPRISE_PRICE = 22

bachelorette_party_price = float(input())
love_letter_count = int(input())
rose_count = int(input())
keykeeper_count = int(input())
cartoon_count = int(input())
lucky_surprise_count = int(input())

love_letter_sum = love_letter_count * LOVE_LETTER_PRICE
rose_sum = rose_count * ROSE_PRICE
keykeeper_sum = keykeeper_count * KEYKEEPER_PRICE
cartoon_sum = cartoon_count * CARTOON_PRICE
lucky_surprise_sum = lucky_surprise_count * LUCKY_SURPRISE_PRICE
total_sum = love_letter_sum + rose_sum + keykeeper_sum + cartoon_sum + lucky_surprise_sum
total_items_count = love_letter_count + rose_count + keykeeper_count + cartoon_count + lucky_surprise_count

if total_items_count >= 25:
    total_sum -= total_sum * 0.35

hosting_cost = total_sum * 0.1
total_sum -= hosting_cost
diff = abs(total_sum - bachelorette_party_price)

if total_sum >= bachelorette_party_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")