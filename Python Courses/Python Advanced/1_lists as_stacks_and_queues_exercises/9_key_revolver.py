from collections import deque

bullet_price = int(input())
barrel_size = int(input())

bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))

intelligence_value = int(input())

bullets_fired = 0

while bullets and locks:
    bullet = bullets.pop()
    lock = locks[0]

    bullets_fired += 1

    if bullet <= lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    if bullets_fired % barrel_size == 0 and bullets:
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money_earned = intelligence_value - bullets_fired * bullet_price
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")