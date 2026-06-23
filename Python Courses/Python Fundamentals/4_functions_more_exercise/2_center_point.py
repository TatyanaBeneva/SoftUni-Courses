from math import floor

def closest_point_to_center(x1, y1, x2, y2):
    first_distance = x1 * x1 + y1 * y1
    second_distance = x2 * x2 + y2 * y2

    if first_distance <= second_distance:
        return f"({floor(x1)}, {floor(y1)})"
    else:
        return f"({floor(x2)}, {floor(y2)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(closest_point_to_center(x1, y1, x2, y2))