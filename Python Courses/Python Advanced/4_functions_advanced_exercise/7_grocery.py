def grocery_store(**kwargs):
    sorted_receipt = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))

    return "\n".join(f"{product}: {quantity}" for product, quantity in sorted_receipt)



print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
