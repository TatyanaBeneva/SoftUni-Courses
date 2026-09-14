from collections import deque

quantity = int(input())
orders = deque(map(int, input().split()))

biggest_client = max(orders)
print(biggest_client)

for _ in range(len(orders)):
    if quantity >= orders[0]:
        quantity -= orders[0]
        orders.popleft()
    else:
        print(f'Orders left: {" ".join(str(o) for o in orders)}')
        break

if not orders:
    print("Orders complete")