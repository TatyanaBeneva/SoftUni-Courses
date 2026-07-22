import re

furniture = []
total_cost = 0.0

pattern = r">>([A-Za-z]+)<<(\d+(?:\.\d+)?)!(\d+)"

while True:
    line = input()

    if line == "Purchase":
        break

    match = re.fullmatch(pattern, line)

    if match is None:
        continue

    name, price, quantity = match.groups()

    furniture.append(name)
    total_cost += float(price) * int(quantity)

print("Bought furniture:")

for name in furniture:
    print(name)

print(f"Total money spend: {total_cost:.2f}")