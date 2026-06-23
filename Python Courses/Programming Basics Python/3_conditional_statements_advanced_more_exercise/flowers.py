chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_festival_day = input()

chrysanthemums_price = 0.00
roses_price = 0.00
tulips_price = 0.00
buket_price = 0.00

if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2
    roses_price = 4.1
    tulips_price = 2.5
elif season == "Winter" or season == "Autumn":
    chrysanthemums_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15

if is_festival_day == "Y":
    chrysanthemums_price += chrysanthemums_price * 0.15
    roses_price += roses_price * 0.15
    tulips_price += tulips_price * 0.15

buket_price = chrysanthemums_price * chrysanthemums_count + roses_price * roses_count + tulips_price * tulips_count

if season == "Spring" and tulips_count > 7:
    buket_price -= buket_price * 0.05

if season == "Winter" and roses_count >= 10:
    buket_price -= buket_price * 0.1

if (chrysanthemums_count + roses_count + tulips_count) > 20:
    buket_price -= buket_price * 0.2

total_buket_price = buket_price + 2

print(f"{total_buket_price:.2f}")