ONE_DISH = 5
ONE_SAUCEPAN = 15
ONE_BOTTLE = 750

bottles_count = int(input())
command = input()
counter = 1
dished_counter = 0
saucepan_counter = 0

available_detergent = ONE_BOTTLE * bottles_count

while command != 'End':
    dishes_count = int(command)

    if counter % 3 == 0:
        available_detergent -= dishes_count * ONE_SAUCEPAN
        saucepan_counter += dishes_count
    else:
        available_detergent -= dishes_count * ONE_DISH
        dished_counter += dishes_count

    if available_detergent < 0:
        break

    counter += 1
    command = input()

if available_detergent >= 0:
    print("Detergent was enough!")
    print(f"{dished_counter} dishes and {saucepan_counter} pots were washed.")
    print(f"Leftover detergent {available_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(available_detergent)} ml. more necessary!")