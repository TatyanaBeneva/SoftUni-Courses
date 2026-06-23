PLAY_IN_WORK_DAYS_MINUTES = 63
PLAY_IN_REST_DAYS_MINUTES = 127
TOTAL_CAT_PLAY_MINUTES_IN_YEAR = 30000
DAYS_IN_YEAR = 365

rest_days_count = int(input())

work_days_count = DAYS_IN_YEAR - rest_days_count
total_rest_days_play_minutes = rest_days_count * PLAY_IN_REST_DAYS_MINUTES
total_work_days_play_minutes = work_days_count * PLAY_IN_WORK_DAYS_MINUTES
total_play_minutes = total_rest_days_play_minutes + total_work_days_play_minutes

if total_play_minutes <= TOTAL_CAT_PLAY_MINUTES_IN_YEAR:
    minutes_that_left = TOTAL_CAT_PLAY_MINUTES_IN_YEAR - total_play_minutes
    hours_left = minutes_that_left // 60
    minutes_left = minutes_that_left % 60
    print("Tom sleeps well")
    print(f"{hours_left} hours and {minutes_left} minutes less for play")
else:
    minutes_that_left = total_play_minutes - TOTAL_CAT_PLAY_MINUTES_IN_YEAR
    hours_left = minutes_that_left // 60
    minutes_left = minutes_that_left % 60
    print("Tom will run away")
    print(f"{hours_left} hours and {minutes_left} minutes more for play")