annual_tax = int(input())

snickers_price = annual_tax * 0.6
team_price = snickers_price * 0.8
ball_price = team_price * 0.25
accessories_price = ball_price * 0.2

total_price = ball_price + accessories_price + team_price + snickers_price + annual_tax
print(f"{total_price:.2f}")