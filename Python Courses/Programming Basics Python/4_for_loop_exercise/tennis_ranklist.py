from math import floor

tournaments_count = int(input())
start_points = int(input())

tournaments_points = 0
win_tournaments = 0

for i in range(tournaments_count):
    tournament_fase = input()

    if tournament_fase == "W":
        tournaments_points += 2000
        win_tournaments += 1
    elif tournament_fase == 'F':
        tournaments_points += 1200
    elif tournament_fase == 'SF':
        tournaments_points += 720

total_points = tournaments_points + start_points
average_points = tournaments_points / tournaments_count
win_rate = (win_tournaments / tournaments_count) * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{win_rate:.2f}%")