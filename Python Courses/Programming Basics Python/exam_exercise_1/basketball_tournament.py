win_games = 0
lost_games = 0

while True:
    command = input()

    if command == "End of tournaments":
        break

    tournament_name = command
    tournament_games_count = int(input())
    games_counter = 0

    for game in range(tournament_games_count):
        desi_team_points = int(input())
        opposite_team_points = int(input())
        games_counter += 1
        points_difference = abs(desi_team_points - opposite_team_points)

        if desi_team_points > opposite_team_points:
            win_games += 1
            print(f"Game {games_counter} of tournament {tournament_name}: win with {points_difference} points.")
        else:
            lost_games += 1
            print(f"Game {games_counter} of tournament {tournament_name}: lost with {points_difference} points.")

all_games = win_games + lost_games

print(f"{win_games / all_games * 100:.2f}% matches win")
print(f"{lost_games / all_games * 100:.2f}% matches lost")
