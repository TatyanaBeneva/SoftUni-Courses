budget = int(input())
season = input()
fishman_count = int(input())

boat_price = 0

if season == "Spring":
    boat_price = 3000
elif (season == "Summer") or (season == "Autumn"):
    boat_price = 4200
elif season == "Winter":
    boat_price = 2600

if fishman_count <= 6:
    boat_price -= boat_price * 0.1
elif 7 <= fishman_count <= 11:
    boat_price -= boat_price * 0.15
elif 11 < fishman_count:
    boat_price -= boat_price * 0.25

if (season != "Autumn") and (fishman_count % 2 == 0):
    boat_price -= boat_price * 0.05

if budget >= boat_price:
    print(f"Yes! You have {budget - boat_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {boat_price - budget:.2f} leva.")