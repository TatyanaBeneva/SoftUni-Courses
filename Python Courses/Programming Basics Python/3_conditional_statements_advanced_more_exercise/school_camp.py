season = input()
group_type = input()
student_count = int(input())
night_count = int(input())

price_for_one_night = 0.0
sport_type = ""

if group_type == "girls":
    if season == "Winter":
        price_for_one_night = 9.6
        sport_type = "Gymnastics"
    elif season == "Spring":
        price_for_one_night = 7.2
        sport_type = "Athletics"
    elif season == "Summer":
        price_for_one_night = 15
        sport_type = "Volleyball"
elif group_type == "boys":
    if season == "Winter":
        price_for_one_night = 9.6
        sport_type = "Judo"
    elif season == "Spring":
        price_for_one_night = 7.2
        sport_type = "Tennis"
    elif season == "Summer":
        price_for_one_night = 15
        sport_type = "Football"
elif group_type == "mixed":
    if season == "Winter":
        price_for_one_night = 10
        sport_type = "Ski"
    elif season == "Spring":
        price_for_one_night = 9.5
        sport_type = "Cycling"
    elif season == "Summer":
        price_for_one_night = 20
        sport_type = "Swimming"

if 10 <= student_count < 20:
    price_for_one_night -= price_for_one_night * 0.05
elif 20 <= student_count < 50:
    price_for_one_night -= price_for_one_night * 0.15
elif student_count >= 50:
    price_for_one_night -= price_for_one_night * 0.5

total_price = student_count * price_for_one_night * night_count

print(f"{sport_type} {total_price:.2f} lv.")