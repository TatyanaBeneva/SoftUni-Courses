def is_prop_in_dict(key, dictionary):
    if key in dictionary:
        return True
    else:
        return False

n = int(input())
cars = {}

for _ in range(n):
    data = input().split()
    action = data[0]
    name = data[1]

    if action == "register":
        plate = data[2]

        if is_prop_in_dict(name, cars):
            print(f"ERROR: already registered with plate number {plate}")
        else:
            cars[name] = plate
            print(f"{name} registered {plate} successfully")
    elif action == "unregister":
        if is_prop_in_dict(name, cars):
            del cars[name]
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for key, value in cars.items():
    print(f"{key} => {value}")