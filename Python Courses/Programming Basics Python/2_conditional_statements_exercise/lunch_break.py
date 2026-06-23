from math import ceil

movie_name = input()
episode_duration = int(input())
all_time = int(input())

lunch_time = all_time * (1 / 8)
rest_time = all_time * (1 / 4)

sum_time = episode_duration + lunch_time + rest_time

if sum_time > all_time:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(sum_time - all_time)} more minutes.")
else:
    print(f"You have enough time to watch {movie_name} and left with {ceil(all_time - sum_time)} minutes free time.")