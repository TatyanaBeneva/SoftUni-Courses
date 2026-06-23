hours = int(input())
minutes = int(input()) + 15
time = "00:00"

if minutes < 60:
    time = f'{hours}:{minutes}'
else:
    hours += 1
    minutes -= 60

    if hours > 23:
        hours -= 24

    if minutes < 10:
        time = f'{hours}:0{minutes}'
    else:
        time = f'{hours}:{minutes}'

print(time)