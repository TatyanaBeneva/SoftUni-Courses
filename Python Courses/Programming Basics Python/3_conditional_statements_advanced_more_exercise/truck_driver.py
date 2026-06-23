season = input()
kilometers = float(input())

total_profit = 0.0

if kilometers <= 5000:
    if season == "Spring" or season == "Autumn":
        total_profit = kilometers * 0.75 * 4
    elif season == "Summer":
        total_profit = kilometers * 0.9 * 4
    elif season == "Winter":
        total_profit = kilometers * 1.05 * 4
elif 5000 < kilometers <= 10000:
    if season == "Spring" or season == "Autumn":
        total_profit = kilometers * 0.95 * 4
    elif season == "Summer":
        total_profit = kilometers * 1.1 * 4
    elif season == "Winter":
        total_profit = kilometers * 1.25 * 4
elif 10000 < kilometers <= 20000:
    total_profit = kilometers * 1.45 * 4

total_profit_after_taxes = total_profit - (total_profit * 0.1)

print(f"{total_profit_after_taxes:.2f}")