def rectangle(length, height):
    if not isinstance(length, int) or not isinstance(height, int):
        return "Enter valid values!"

    def area():
        return length * height

    def perimeter():
        return 2 * (length + height)

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"



print(rectangle(2, 10))
print(rectangle('2', 10))