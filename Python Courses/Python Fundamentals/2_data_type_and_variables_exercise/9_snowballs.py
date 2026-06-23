snowballs_number = int(input())
snowball_highest_value = 0
snowball_highest_weight = 0
snowball_highest_time = 0
snowball_highest_quality = 0

for i in range(snowballs_number):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight // snowball_time) ** snowball_quality

    if snowball_value > snowball_highest_value:
        snowball_highest_value = snowball_value
        snowball_highest_weight = snowball_weight
        snowball_highest_time = snowball_time
        snowball_highest_quality = snowball_quality

print(f"{snowball_highest_weight} : {snowball_highest_time} = {snowball_highest_value} ({snowball_highest_quality})")