hour = int(input())
day_of_the_week = input()

result = ""

if (day_of_the_week == "Monday"
    or day_of_the_week == "Tuesday"
    or day_of_the_week == "Wednesday"
    or day_of_the_week == "Thursday"
    or day_of_the_week == "Friday"
    or day_of_the_week == "Saturday"
    ) and 10 <= hour <= 18:
    result = "open"
else:
    result = "closed"

print(result)