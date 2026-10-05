def plant_garden(available_garden_space: float, *args, **kwargs):
    from decimal import Decimal

    available_garden_space = Decimal(str(available_garden_space))
    allowed_plants = dict(args)
    planted_plants = {}
    all_planted = True

    for plant_type, quantity in sorted(kwargs.items()):
        if plant_type not in allowed_plants:
            continue

        space_per_plant = Decimal(str(allowed_plants[plant_type]))
        planted_quantity = min(quantity, int(available_garden_space // space_per_plant))

        if planted_quantity > 0:
            planted_plants[plant_type] = planted_quantity
            available_garden_space -= planted_quantity * space_per_plant

        if planted_quantity < quantity:
            all_planted = False

    if all_planted:
        result = [f"All plants were planted! Available garden space: {available_garden_space:.1f} sq meters."]
    else:
        result = ["Not enough space to plant all requested plants!"]

    result.append("Planted plants:")

    for key, value in planted_plants.items():
        result.append(f"{key}: {value}")

    return "\n".join(result)


if __name__ == "__main__":
    print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
    print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
    print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
    print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))
