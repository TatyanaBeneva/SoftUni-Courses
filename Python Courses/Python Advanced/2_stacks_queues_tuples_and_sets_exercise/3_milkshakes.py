from collections import deque

chocolates = list(map(int, input().split(", ")))
cups_of_milk = deque(map(int, input().split(", ")))

milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    chocolate = chocolates.pop()
    milk = cups_of_milk.popleft()

    if chocolate <= 0 and milk <= 0:
        continue

    if chocolate <= 0:
        cups_of_milk.appendleft(milk)
        continue

    if milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        cups_of_milk.append(milk)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(map(str, cups_of_milk))}")
else:
    print("Milk: empty")