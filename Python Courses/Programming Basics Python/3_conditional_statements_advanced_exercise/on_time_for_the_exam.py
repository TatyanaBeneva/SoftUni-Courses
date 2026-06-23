exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

all_exam_minutes = exam_hour * 60 + exam_minute
all_arrive_minutes = arrive_hour * 60 + arrive_minute
difference_time = all_exam_minutes - all_arrive_minutes

if difference_time == 0:
    print("On time")
elif 0 < difference_time <= 30:
    print("On time")
    print(f"{difference_time} minutes before the start")
elif 0 < difference_time:
    print("Early")
    if difference_time < 60:
        print(f"{difference_time} minutes before the start")
    else:
        hours = difference_time // 60
        minutes = difference_time % 60

        print(f"{hours}:{minutes:02d} hours before the start")
elif -60 < difference_time < 0:
    print("Late")
    print(f"{abs(difference_time)} minutes after the start")
elif difference_time <= -60:
    print("Late")
    hours = abs(difference_time) // 60
    minutes = abs(difference_time) % 60

    print(f"{hours}:{minutes:02d} hours after the start")
