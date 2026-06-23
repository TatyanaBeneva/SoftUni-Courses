cargo_counts = int(input())

minibus = 0
truck = 0
train = 0

price = 0
all_cargo_tons = 0

for i in range(cargo_counts):
    cargo_tons = int(input())

    if cargo_tons <= 3:
        minibus += cargo_tons
        price += cargo_tons * 200
    elif 4 <= cargo_tons <= 11:
        truck += cargo_tons
        price += cargo_tons * 175
    elif cargo_tons >= 12:
        train += cargo_tons
        price += cargo_tons * 120

    all_cargo_tons += cargo_tons

print(f"{price / all_cargo_tons:.2f}")
print(f"{minibus / all_cargo_tons * 100:.2f}%")
print(f"{truck / all_cargo_tons * 100:.2f}%")
print(f"{train / all_cargo_tons * 100:.2f}%")