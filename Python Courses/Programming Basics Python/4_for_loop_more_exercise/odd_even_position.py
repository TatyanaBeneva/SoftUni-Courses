n = int(input())

odd_sum = 0.0
odd_min = float('inf')
odd_max = float('-inf')

even_sum = 0.0
even_min = float('inf')
even_max = float('-inf')

for i in range(1, n + 1):
    num = float(input())

    if i % 2 != 0:
        odd_sum += num
        if num < odd_min: odd_min = num
        if num > odd_max: odd_max = num
    else:
        even_sum += num
        if num < even_min: even_min = num
        if num > even_max: even_max = num


def format_val(val):
    if val == float('inf') or val == float('-inf'):
        return "No"
    return f"{val:.2f}"


print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={format_val(odd_min)},")
print(f"OddMax={format_val(odd_max)},")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={format_val(even_min)},")
print(f"EvenMax={format_val(even_max)}")
