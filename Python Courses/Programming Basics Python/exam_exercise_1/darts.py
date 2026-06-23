STARTING_POINTS = 301

player_name = input()

remaining_points = STARTING_POINTS
successful_shots = 0
unsuccessful_shots = 0

while True:
    field = input()

    if field == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break

    points = int(input())

    if field == "Double":
        points *= 2
    elif field == "Triple":
        points *= 3

    if points > remaining_points:
        unsuccessful_shots += 1
        continue

    remaining_points -= points
    successful_shots += 1

    if remaining_points == 0:
        print(f"{player_name} won the leg with {successful_shots} shots.")
        break