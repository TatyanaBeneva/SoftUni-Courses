annual_tax = int(input())

basketball_sneakers_price = annual_tax - (annual_tax * 0.4)
basketball_team_price = basketball_sneakers_price - (basketball_sneakers_price * 0.2)
basketball_ball_price = basketball_team_price / 4
basketball_accessories_price = basketball_ball_price / 5

total_sum = annual_tax + basketball_sneakers_price + basketball_team_price + basketball_ball_price + basketball_accessories_price

print(total_sum)
