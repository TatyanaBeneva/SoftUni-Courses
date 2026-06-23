from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())

extra_time = floor(distance_in_meters / 15) * 12.5
total_seconds = distance_in_meters * time_in_seconds + extra_time

if total_seconds < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {total_seconds:.2f} seconds.')
else:
    print(f'No, he failed! He was {(total_seconds - record_in_seconds):.2f} seconds slower.')