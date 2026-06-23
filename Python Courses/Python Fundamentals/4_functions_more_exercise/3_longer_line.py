from math import floor

def closest_point_to_center(x1, y1, x2, y2):
    first_distance = x1 * x1 + y1 * y1
    second_distance = x2 * x2 + y2 * y2

    if first_distance <= second_distance:
        return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
    else:
        return f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"

def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    first_distance = (x1 * x1 + y1 * y1) + (x2 * x2 + y2 * y2)
    second_distance = (x3 * x3 + y3 * y3) + (x4 * x4 + y4 * y4)

    if first_distance >= second_distance:
        return closest_point_to_center(x1, y1, x2, y2)
    else:
        return closest_point_to_center(x3, y3, x4, y4)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))