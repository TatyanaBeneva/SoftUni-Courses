VIP_TICKET_PRICE = 499.99
NORMAL_TICKET_PRICE = 249.99

budget = float(input())
ticket_category = input()
people_count = int(input())

transport_expenses = 0.00
ticket_expenses = 0.00

if 1 <= people_count <=4:
    transport_expenses = budget * 0.75
elif 5 <= people_count <= 9:
    transport_expenses = budget * 0.60
elif 10 <= people_count <= 24:
    transport_expenses = budget * 0.50
elif 24 <= people_count <= 49:
    transport_expenses = budget * 0.40
elif 50 <= people_count:
    transport_expenses = budget * 0.25

if ticket_category == "VIP":
    ticket_expenses = VIP_TICKET_PRICE * people_count
elif ticket_category == "Normal":
    ticket_expenses = NORMAL_TICKET_PRICE * people_count

sum_of_expenses = transport_expenses + ticket_expenses

if sum_of_expenses <= budget:
    print(f"Yes! You have {budget - sum_of_expenses:.2f} leva left.")
else:
    print(f"Not enough money! You need {sum_of_expenses - budget:.2f} leva.")