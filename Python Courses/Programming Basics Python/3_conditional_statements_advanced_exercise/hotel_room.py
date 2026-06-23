month = input()
nights_count = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50 * nights_count
    apartment_price = 65 * nights_count

    if 7 < nights_count <= 14:
        studio_price -= studio_price * 0.05
    elif nights_count > 14:
        studio_price -= studio_price * 0.3
elif month == "June" or month == "September":
    studio_price = 75.20 * nights_count
    apartment_price = 68.70 * nights_count

    if nights_count > 14:
        studio_price -= studio_price * 0.2
elif month == "July" or month == "August":
    studio_price = 76 * nights_count
    apartment_price = 77 * nights_count

if nights_count > 14:
    apartment_price -= apartment_price * 0.1

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
