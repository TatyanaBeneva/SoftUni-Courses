vegi_kilo_price = float(input())
fruit_kilo_price = float(input())
vegi_kilo_count = float(input())
fruit_kilo_count = float(input())

vegi_sum = vegi_kilo_price * vegi_kilo_count
fruit_sum = fruit_kilo_count * fruit_kilo_price

total_sum_euro = (vegi_sum + fruit_sum) / 1.94

print(f'{total_sum_euro:.2f}')
