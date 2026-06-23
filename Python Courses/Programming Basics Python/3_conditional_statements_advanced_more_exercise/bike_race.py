junior_bikers = int(input())
senior_bikers = int(input())
trace_type = input()

total_sum = 0.00

if trace_type == "trail":
    total_sum = junior_bikers * 5.5 + senior_bikers * 7
elif trace_type == "cross-country":
    total_sum = junior_bikers * 8 + senior_bikers * 9.5

    if junior_bikers + senior_bikers >= 50:
        total_sum -= total_sum * 0.25

elif trace_type == "downhill":
    total_sum = junior_bikers * 12.25 + senior_bikers * 13.75
elif trace_type == "road":
    total_sum = junior_bikers * 20 + senior_bikers * 21.5

total_sum -= total_sum * 0.05

print(f"{total_sum:.2f}")