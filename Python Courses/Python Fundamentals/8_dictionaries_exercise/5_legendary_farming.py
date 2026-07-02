items_dict = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

is_item_obtained = False

while not is_item_obtained:
    items_list = input().split()

    for i in range(0, len(items_list), 2):
        item = items_list[i + 1].lower()
        quantity = int(items_list[i])

        if item not in items_dict:
            items_dict[item] = quantity
        else:
            items_dict[item] += quantity

        if item in ["shards", "fragments", "motes"] and items_dict[item] >= 250:
            match item:
                case "shards":
                    print("Shadowmourne obtained!")
                case "fragments":
                    print("Valanyr obtained!")
                case "motes":
                    print("Dragonwrath obtained!")

            items_dict[item] -= 250
            is_item_obtained = True
            break

print(f"shards: {items_dict['shards']}")
print(f"fragments: {items_dict['fragments']}")
print(f"motes: {items_dict['motes']}")

for key, value in items_dict.items():
    if key not in ["shards", "fragments", "motes"]:
        print(f"{key}: {value}")