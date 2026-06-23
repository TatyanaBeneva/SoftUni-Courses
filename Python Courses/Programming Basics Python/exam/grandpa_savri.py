days = int(input())

all_brandy_liters = 0.0
all_brandy_degrees = 0.0

for day in range(days):
    brandy_liters = float(input())
    brandy_degrees = float(input())

    all_brandy_liters += brandy_liters
    all_brandy_degrees += brandy_degrees * brandy_liters

average_brandy_degrees = all_brandy_degrees / all_brandy_liters

print(f"Liter: {all_brandy_liters:.2f}")
print(f"Degrees: {average_brandy_degrees:.2f}")

if average_brandy_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_brandy_degrees <= 42:
    print("Super!")
elif 42 < average_brandy_degrees:
    print("Dilution with distilled water!")