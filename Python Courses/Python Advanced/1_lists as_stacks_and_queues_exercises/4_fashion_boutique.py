from collections import deque

clothes = deque([int(item) for item in input().split()])
capacity = int(input())
capacity_clone = capacity
racks = 1

for _ in range(len(clothes)):
    last_patch = clothes.pop()

    if capacity_clone < last_patch:
        capacity_clone = capacity
        racks += 1

    capacity_clone -= last_patch

print(racks)