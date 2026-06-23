from math import floor, ceil

x = int(input())
y = float(input())
z = int(input())
workers = int(input())

total_grape = x * y
wine = 0.4 * (total_grape / 2.5)

if wine >= z:
    litters_wine_left = wine - z
    litters_per_worker = litters_wine_left / workers
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(litters_wine_left)} liters left -> {ceil(litters_per_worker)} liters per person.")
else:
    litters_wine_needed = z - wine
    print(f"It will be a tough winter! More {floor(litters_wine_needed)} liters wine needed.")
