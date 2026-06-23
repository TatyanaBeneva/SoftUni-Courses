volume  = int(input())
p1 = int(input())
p2 = int(input())
hours = float(input())

p1_volume = p1 * hours
p2_volume = p2 * hours
volume_sum = p1_volume + p2_volume

if volume_sum <= volume:
    pool_volume_percent = (volume_sum / volume) * 100
    p1_volume_percent = (p1_volume / volume_sum) * 100
    p2_volume_percent = (p2_volume / volume_sum) * 100
    print(f"The pool is {pool_volume_percent:.2f}% full. Pipe 1: {p1_volume_percent:.2f}%. Pipe 2: {p2_volume_percent:.2f}%.")
else:
    print(f"For {hours} hours the pool overflows with {(volume_sum - volume):.2f} liters.")