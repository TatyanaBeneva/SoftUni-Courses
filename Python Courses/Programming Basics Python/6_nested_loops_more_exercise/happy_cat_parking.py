days = int(input())
hours = int(input())

total_sum = 0

for day in range(1, days + 1):
    day_sum = 0

    for hour in range(1, hours + 1):

        if day % 2 == 0 and hour % 2 != 0:
            price = 2.50

        elif day % 2 != 0 and hour % 2 == 0:
            price = 1.25

        else:
            price = 1

        day_sum += price

    total_sum += day_sum

    print(f"Day: {day} - {day_sum:.2f} leva")

print(f"Total: {total_sum:.2f} leva")