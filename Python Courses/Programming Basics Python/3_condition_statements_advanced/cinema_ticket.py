day_of_the_week = input()

price = 0

if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Friday":
    price = 12
elif day_of_the_week == "Wednesday" or day_of_the_week == "Thursday":
    price = 14
elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    price = 16

print(price)