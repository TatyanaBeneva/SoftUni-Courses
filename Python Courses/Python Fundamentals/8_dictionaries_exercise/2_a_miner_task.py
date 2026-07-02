resources = {}

while True:
    data = input()

    if data == "stop":
        break

    quantity = int(input())

    if data not in resources:
        resources[data] = quantity
    else:
        resources[data] += quantity

for key, value in resources.items():
    print(f"{key} -> {value}")
