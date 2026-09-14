from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
cars_passed = 0
crash = False

while True:
    command = input()

    if command == "END":
        break

    if command != "green":
        cars.append(command)
        continue

    current_green = green_light

    while cars and current_green > 0:
        car = cars.popleft()

        if len(car) <= current_green:
            current_green -= len(car)
            cars_passed += 1

        else:
            remaining_car = car[current_green:]
            current_green = 0

            if len(remaining_car) <= free_window:
                cars_passed += 1
            else:
                hit_character = remaining_car[free_window]

                print("A crash happened!")
                print(f"{car} was hit at {hit_character}.")

                crash = True
                break

    if crash:
        break

if not crash:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")