from math import floor

biscuits_per_worker = int(input())
workers_count = int(input())
competing_factory_produce = int(input())
produced_biscuits = 0

for day in range(1, 31):
    daily_production = biscuits_per_worker * workers_count

    if day % 3 == 0:
        produced_biscuits += floor(daily_production * 0.75)
    else:
        produced_biscuits += daily_production

diff_percentage = abs(competing_factory_produce - produced_biscuits) / competing_factory_produce * 100
print(f"You have produced {produced_biscuits} biscuits for the past month.")

if competing_factory_produce > produced_biscuits:
    print(f"You produce {diff_percentage:.2f} percent less biscuits.")
else:
    print(f"You produce {diff_percentage:.2f} percent more biscuits.")

