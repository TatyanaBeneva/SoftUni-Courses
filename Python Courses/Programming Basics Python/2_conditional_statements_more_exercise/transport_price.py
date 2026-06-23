TAXI_START_TAX = 0.7
TAXI_DAY_TARIFF = 0.79
TAXI_NIGHT_TARIFF = 0.9
AUTOBUS_TARIFF = 0.09
AUTOBUS_MINIMUM_DISTANCE = 20
TRAIN_TARIFF = 0.06
TRAIN_MINIMAL_DISTANCE = 100

kilometers = int(input())
time_of_travel = input()

transport_vehicle = ""
price = 0.00

if kilometers < AUTOBUS_MINIMUM_DISTANCE:
    transport_vehicle = "taxi"
elif kilometers < TRAIN_MINIMAL_DISTANCE:
    transport_vehicle = "autobus"
else:
    transport_vehicle = "train"

if transport_vehicle == "taxi":
    if time_of_travel == "day":
        price = TAXI_START_TAX + (kilometers * TAXI_DAY_TARIFF)
    elif time_of_travel == "night":
        price = TAXI_START_TAX + (kilometers * TAXI_NIGHT_TARIFF)
elif transport_vehicle == "autobus":
    price = kilometers * AUTOBUS_TARIFF
elif transport_vehicle == "train":
    price = kilometers * TRAIN_TARIFF

print(f"{price:.2f}")