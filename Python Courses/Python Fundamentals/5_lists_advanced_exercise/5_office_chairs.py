number_of_rooms = int(input())
total_free_chairs = 0
are_chairs_enough = True

for room_number in range(1, number_of_rooms + 1):
    chairs, visitors = input().split()

    number_of_chairs = len(chairs)
    visitors = int(visitors)

    if number_of_chairs < visitors:
        needed_chairs = visitors - number_of_chairs
        print(f"{needed_chairs} more chairs needed in room {room_number}")
        are_chairs_enough = False
    else:
        total_free_chairs += number_of_chairs - visitors

if are_chairs_enough:
    print(f"Game On, {total_free_chairs} free chairs left")