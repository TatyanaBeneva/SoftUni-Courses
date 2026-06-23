def sum_numbers(num1: int, num2: int):
    return num1 + num2

def subtract(num1: int, num2: int, num3: int):
    return sum_numbers(num1, num2) - num3

def add_and_subtract(num1: int, num2: int, num3: int):
    print(subtract(num1, num2, num3))

num1 = int(input())
num2 = int(input())
num3 = int(input())

add_and_subtract(num1, num2, num3)