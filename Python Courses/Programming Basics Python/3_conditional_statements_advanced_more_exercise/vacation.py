budget = float(input())
season = input()

location = ""
place_of_stay = ""
total_price = 0.0

if budget <= 1000:
    place_of_stay = "Camp"

    if season == "Summer":
        total_price = budget * 0.65
    elif season == "Winter":
        total_price = budget * 0.45
elif 1000< budget <= 3000:
    place_of_stay = "Hut"

    if season == "Summer":
        total_price = budget * 0.8
    elif season == "Winter":
        total_price = budget * 0.6
elif budget > 3000:
    place_of_stay = "Hotel"
    total_price = budget * 0.9

if season == "Summer":
    location = "Alaska"
elif season == "Winter":
    location = "Morocco"

print(f"{location} - {place_of_stay} - {total_price:.2f}")