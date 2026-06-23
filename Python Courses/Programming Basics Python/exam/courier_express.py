package_weight = float(input())
service_type = input()
distance = int(input())

price_per_kilometer = 0.0
surcharge_per_kilometer = 0.0
total_sum = 0.0

if package_weight < 1:
    price_per_kilometer = 0.03
elif 1 <= package_weight < 10:
    price_per_kilometer = 0.05
elif 10 <= package_weight <= 40:
    price_per_kilometer = 0.10
elif 40 < package_weight <= 90:
    price_per_kilometer = 0.15
elif 90 < package_weight <= 150:
    price_per_kilometer = 0.20

total_sum = distance * price_per_kilometer

if service_type == "express":
    if package_weight < 1:
        surcharge_per_kilometer = package_weight * (0.03 * 0.8)
    elif 1 <= package_weight < 10:
        surcharge_per_kilometer = package_weight * (0.05 * 0.4)
    elif 10 <= package_weight <= 40:
        surcharge_per_kilometer = package_weight * (0.10 * 0.05)
    elif 40 < package_weight <= 90:
        surcharge_per_kilometer = package_weight * (0.15 * 0.02)
    elif 90 < package_weight <= 150:
        surcharge_per_kilometer = package_weight * (0.20 * 0.01)

    total_sum += surcharge_per_kilometer * distance

print(f"The delivery of your shipment with weight of {package_weight:.3f} kg. would cost {total_sum:.2f} lv.")