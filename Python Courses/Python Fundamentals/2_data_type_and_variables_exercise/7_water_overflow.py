tank_capacity = 255
n = int(input())
tank_litters = 0

for i in range(n):
    litters_of_water = int(input())

    if tank_litters + litters_of_water > tank_capacity:
        print("Insufficient capacity!")
    else:
        tank_litters += litters_of_water

print(tank_litters)