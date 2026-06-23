INITIAL_ENERGY = 100
INITIAL_COINS = 100

events = input().split("|")
energy = INITIAL_ENERGY
coins = INITIAL_COINS
is_day_completed = True

for event in events:
    event_list = event.split("-")
    event_type = event_list[0]
    event_amount = int(event_list[1])

    if event_type == "rest":
        gained_energy = min(event_amount, INITIAL_ENERGY - energy)
        energy += gained_energy

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_type == "order":
        if energy >= 30:
            energy -= 30
            coins += event_amount
            print(f"You earned {event_amount} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= event_amount:
            coins -= event_amount
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}." )
            is_day_completed = False
            break

if is_day_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")