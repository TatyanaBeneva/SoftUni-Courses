fuel_type = input()
fuel_litters = int(input())

if fuel_type == "Diesel" or fuel_type == "Gas" or fuel_type == "Gasoline":
    if fuel_litters < 25:
        print(f"Fill your tank with {fuel_type.lower()}!")
    else:
        print(f"You have enough {fuel_type.lower()}.")
else:
    print("Invalid fuel!")