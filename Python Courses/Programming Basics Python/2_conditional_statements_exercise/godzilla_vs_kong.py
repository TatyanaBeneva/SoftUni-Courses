movie_budget = float(input())
statistics_count = int(input())
statistic_dress_price = float(input())

sum_movie_decor = movie_budget * 0.1
sum_dress = statistics_count * statistic_dress_price

if statistics_count > 150:
    sum_dress = sum_dress - (sum_dress * 0.1)

total_movie_sum = sum_movie_decor + sum_dress

if total_movie_sum > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {(total_movie_sum - movie_budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(movie_budget - total_movie_sum):.2f} leva left.")