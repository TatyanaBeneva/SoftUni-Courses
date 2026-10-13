from collections import deque


def boarding_passengers(available_capacity: int, *passengers):
    passengers = deque(passengers)
    guests = dict()
    is_passenger_more_then_capacity = False
    result = []

    while passengers and available_capacity > 0:
        number_of_passengers, program_name = passengers.popleft()

        if number_of_passengers > available_capacity:
            is_passenger_more_then_capacity = True
            continue

        if program_name not in guests:
            guests[program_name] = 0

        guests[program_name] += number_of_passengers
        available_capacity -= number_of_passengers

    sorted_guests = sorted(guests.items(), key=lambda kvp: (-kvp[1], kvp[0]))

    result.append("Boarding details by benefit plan:")

    for guest in sorted_guests:
        result.append(f"## {guest[0]}: {guest[1]} guests")

    if not passengers and not is_passenger_more_then_capacity:
        result.append("All passengers are successfully boarded!")
    elif not available_capacity and passengers:
        result.append("Boarding unsuccessful. Cruise ship at full capacity.")
    elif available_capacity and is_passenger_more_then_capacity:
        result.append(f"Partial boarding completed. Available capacity: {available_capacity}.")

    return "\n".join(result)


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))