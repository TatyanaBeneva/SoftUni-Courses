from collections import deque

n = int(input())

pumps = deque()

for _ in range(n):
    petrol, distance = map(int, input().split())
    pumps.append((petrol, distance))

for start_index in range(n):
    tank = 0
    completed = True

    for petrol, distance in pumps:
        tank += petrol

        if tank < distance:
            completed = False
            break

        tank -= distance

    if completed:
        print(start_index)
        break

    pumps.rotate(-1)