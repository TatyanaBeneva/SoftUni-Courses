from collections import deque

cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))

wasted_water = 0

while cups and bottles:
    bottle = bottles.pop()
    cup = cups[0]

    if bottle >= cup:
        wasted_water += bottle - cup
        cups.popleft()
    else:
        cups[0] -= bottle

if not cups:
    print(f"Bottles: {' '.join(str(x) for x in reversed(bottles))}")
else:
    print(f"Cups: {' '.join(str(x) for x in cups)}")

print(f"Wasted litters of water: {wasted_water}")