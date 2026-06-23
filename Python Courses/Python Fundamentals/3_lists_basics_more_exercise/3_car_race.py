sequence_of_numbers = input().split(" ")
numbers_list = list(map(int, sequence_of_numbers))
half_of_the_numbers = len(numbers_list) // 2
total_left_time = 0.0
total_right_time = 0.0

for i in range(half_of_the_numbers):
    current_left_time = numbers_list[i]
    current_right_time = numbers_list[len(numbers_list) - 1 - i]

    if current_left_time == 0:
        total_left_time *= 0.8
    else:
        total_left_time += current_left_time

    if current_right_time == 0:
        total_right_time *= 0.8
    else:
        total_right_time += current_right_time

winner = ""
winner_time = 0.0

if total_left_time < total_right_time:
    winner = "left"
    winner_time = total_left_time
else:
    winner = "right"
    winner_time = total_right_time

print(f"The winner is {winner} with total time: {winner_time:.1f}")