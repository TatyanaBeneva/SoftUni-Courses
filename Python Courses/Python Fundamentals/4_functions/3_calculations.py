input_operator = input()
num_1 = int(input())
num_2 = int(input())

def calculate_numbers(a: int, b: int, operator: str):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = int(a / b)
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b

    return result

print(calculate_numbers(num_1, num_2, input_operator))