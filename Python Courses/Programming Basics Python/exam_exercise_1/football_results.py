won_games = 0
loos_games = 0
equal_games = 0

for i in range(1, 4):
    mach_result = input()
    host_result = mach_result[0]
    guest_result = mach_result[2]

    if host_result > guest_result:
        won_games += 1
    elif host_result < guest_result:
        loos_games += 1
    elif host_result == guest_result:
        equal_games += 1

print(f"Team won {won_games} games.")
print(f"Team lost {loos_games} games.")
print(f"Drawn games: {equal_games}")