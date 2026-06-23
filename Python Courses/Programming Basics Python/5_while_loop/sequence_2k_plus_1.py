n = int(input())
next_number = 0

while True:
    next_number = (next_number * 2) + 1

    if next_number > n:
        break

    print(next_number)