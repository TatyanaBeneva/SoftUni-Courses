from collections import deque


packages_weight = [int(el) for el in input().split()]
couriers_capacities = deque([int(el) for el in input().split()])
total_weight = 0

while couriers_capacities and packages_weight:
    current_package_weight = packages_weight.pop()
    current_courier_capacities = couriers_capacities.popleft()

    if current_courier_capacities >= current_package_weight:
        total_weight += current_package_weight
        current_courier_capacities -= current_package_weight * 2

        if current_courier_capacities > 0:
            couriers_capacities.append(current_courier_capacities)
            continue

    else:
        current_package_weight -= current_courier_capacities
        packages_weight.append(current_package_weight)
        total_weight += current_courier_capacities


print(f"Total weight: {total_weight} kg")

if not couriers_capacities and not packages_weight:
    print(f"Congratulations, all packages were delivered successfully by the couriers today.")
elif not couriers_capacities and packages_weight:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages_weight))}")
elif couriers_capacities and not packages_weight:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers_capacities))} but there are no more packages to deliver.")
