x = float(input())
y = float(input())
h = float(input())

side_wall = x * y
window = 1.5 * 1.5
both_sides = 2 * side_wall - 2 * window
back_side = x * x
front_side = 1.2 * 2
total_both_sides = 2 * back_side - front_side

total_area = both_sides + total_both_sides
green_paint = total_area / 3.4

roof_rectangles = 2 * (x * y)
roof_triangles = 2 * (x * h / 2)

total_roof_area = roof_rectangles + roof_triangles
red_paint = total_roof_area / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')