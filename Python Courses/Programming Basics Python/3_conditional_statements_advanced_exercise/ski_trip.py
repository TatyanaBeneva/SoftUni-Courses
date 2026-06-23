ROOM_FOR_ONE_PERSON_PRICE = 18
APARTMENT_PRICE = 25
PRESIDENT_APARTMENT_PRICE = 35

days = int(input())
room_type = input()
evaluation = input()

total_price = 0

if room_type == "room for one person":
    total_price = ROOM_FOR_ONE_PERSON_PRICE * (days - 1)
elif room_type == "apartment":
    total_price = APARTMENT_PRICE * (days - 1)

    if days < 10:
        total_price -= total_price * 0.3
    elif 10 <= days <= 15:
        total_price -= total_price * 0.35
    elif days > 15:
        total_price -= total_price * 0.5
elif room_type == "president apartment":
    total_price = PRESIDENT_APARTMENT_PRICE * (days - 1)

    if days < 10:
        total_price -= total_price * 0.1
    elif 10 <= days <= 15:
        total_price -= total_price * 0.15
    elif days > 15:
        total_price -= total_price * 0.2

if evaluation == "positive":
    total_price += total_price * 0.25
elif evaluation == "negative":
    total_price -= total_price * 0.1

print(f"{total_price:.2f}")