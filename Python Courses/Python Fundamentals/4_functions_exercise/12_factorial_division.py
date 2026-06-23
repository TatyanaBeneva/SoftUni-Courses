def factorial_of_number(number: int):
    factorial = 1
    if not number == 0 and not number == 1:
        for i in range(1, number + 1):
            factorial *= i

    return factorial

def divide_numbers(num1, num2):
    return num1 / num2

n1 = int(input())
n2 = int(input())

division_of_numbers = divide_numbers(factorial_of_number(n1), factorial_of_number(n2))

print(f"{division_of_numbers:.2f}")