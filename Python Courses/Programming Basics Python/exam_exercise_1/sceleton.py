control_minutes = int(input())
control_seconds = int(input())
width = float(input())
seconds_for_100 = int(input())

control_time_in_seconds = control_minutes * 60 + control_seconds
time_late = (width / 120) * 2.5
total_time_in_seconds = (width / 100) * seconds_for_100 - time_late
result = ""

if control_time_in_seconds >= total_time_in_seconds:
    result = f"Marin Bangiev won an Olympic quota!\nHis time is {total_time_in_seconds:.3f}."
else:
    result = f"No, Marin failed! He was {total_time_in_seconds - control_time_in_seconds:.3f} second slower."

print(result)