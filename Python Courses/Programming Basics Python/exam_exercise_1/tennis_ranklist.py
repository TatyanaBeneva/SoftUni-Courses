from math import floor

tournaments_count = int(input())
started_points = int(input())
total_points = started_points
win_tournaments_count = 0

for i in range(tournaments_count):
    tournament_stage = input()

    if tournament_stage == "W":
        total_points += 2000
        win_tournaments_count += 1
    elif tournament_stage == "F":
        total_points += 1200
    elif tournament_stage == "SF":
        total_points += 720

print(f"Final points: {total_points}")
print(f"Average points: {floor((total_points - started_points) / tournaments_count)}")
print(f"{win_tournaments_count / tournaments_count * 100:.2f}%")