ROSES_PRICE = 5
DAHLIA_PRICE = 3.8
TULIP_PRICE = 2.8
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.5

flower_type = input()
flower_count = int(input())
budget = int(input())

flower_sum = 0

if flower_type == "Roses":
    flower_sum = ROSES_PRICE * flower_count
    if flower_count > 80:
        flower_sum -= (flower_sum * 0.1)
elif flower_type == "Dahlias":
    flower_sum = DAHLIA_PRICE * flower_count
    if flower_count > 90:
        flower_sum -= (flower_sum * 0.15)
elif flower_type == "Tulips":
    flower_sum = TULIP_PRICE * flower_count
    if flower_count > 80:
        flower_sum -= (flower_sum * 0.15)
elif flower_type == "Narcissus":
    flower_sum = NARCISSUS_PRICE * flower_count
    if flower_count < 120:
        flower_sum += (flower_sum * 0.15)
elif flower_type == "Gladiolus":
    flower_sum = GLADIOLUS_PRICE * flower_count
    if flower_count < 80:
        flower_sum += (flower_sum * 0.2)

if flower_sum <= budget:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - flower_sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {flower_sum - budget:.2f} leva more.")

