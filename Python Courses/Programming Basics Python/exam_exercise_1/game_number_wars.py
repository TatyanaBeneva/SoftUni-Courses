first_player_name = input()
second_player_name = input()

first_player_points = 0
second_player_points = 0

while True:
    command = input()

    if command == "End of game":
        print(f"{first_player_name} has {first_player_points} points")
        print(f"{second_player_name} has {second_player_points} points")
        break

    first_player_card = int(command)
    second_player_card = int(input())

    if first_player_card > second_player_card:
        first_player_points += first_player_card - second_player_card

    elif second_player_card > first_player_card:
        second_player_points += second_player_card - first_player_card

    else:
        print("Number wars!")

        first_war_card = int(input())
        second_war_card = int(input())

        if first_war_card > second_war_card:
            print(f"{first_player_name} is winner with {first_player_points} points")
        else:
            print(f"{second_player_name} is winner with {second_player_points} points")

        break