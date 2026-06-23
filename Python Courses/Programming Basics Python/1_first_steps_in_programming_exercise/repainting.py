nylons = int(input())
paint = int(input())
thinner = int(input())
hours_for_working = int(input())

nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00

nylon_sum = (nylons + 2) * nylon_price
paint_sum = (paint + (paint * 0.1)) * paint_price
thinner_sum = thinner * thinner_price

total_sum_for_materials = nylon_sum + paint_sum + thinner_sum + 0.40
master_sum = (total_sum_for_materials * 0.3) * hours_for_working

total_sum = total_sum_for_materials + master_sum

print(total_sum)