from math import ceil, floor

days = int(input())
food_kilo = int(input())
dog_food_kilo = float(input())
cat_food_kilo = float(input())
turtle_food_gram = float(input())

total_dog_food_kilo = days * dog_food_kilo
total_cat_food_kilo = days * cat_food_kilo
total_turtle_food_kilo = (days * turtle_food_gram) / 1000
total_food = total_cat_food_kilo + total_turtle_food_kilo + total_dog_food_kilo

if total_food > food_kilo:
    result = total_food - food_kilo
    print(f"{ceil(result)} more kilos of food are needed.")
else:
    result = food_kilo - total_food
    print(f"{floor(result)} kilos of food left.")