stage = input()
ticket_type = input()
tickets_count = int(input())
with_picture = input()

price = 0
total_price = 0

if ticket_type == "Standard":
    if stage == "Quarter final":
        price = 55.50
    elif stage == "Semi final":
        price = 75.88
    elif stage == "Final":
        price = 110.10
elif ticket_type == "Premium":
    if stage == "Quarter final":
        price = 105.20
    elif stage == "Semi final":
        price = 125.22
    elif stage == "Final":
        price = 160.66
elif ticket_type == "VIP":
    if stage == "Quarter final":
            price = 118.90
    elif stage == "Semi final":
            price = 300.40
    elif stage == "Final":
            price = 400

total_tickets_price = price * tickets_count

if total_tickets_price > 4000:
    total_price = total_tickets_price * 0.75
elif 2500 < total_tickets_price <= 4000:
    total_price = total_tickets_price * 0.90

    if with_picture == "Y":
        total_price += 40 * tickets_count

else:
    total_price = total_tickets_price

    if with_picture == "Y":
        total_price += 40 * tickets_count

print(f"{total_price:.2f}")