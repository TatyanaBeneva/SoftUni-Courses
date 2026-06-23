n1 = int(input())
n2 = int(input())
operator = input()

result = 0

if operator == "+" or operator == "-" or operator == "*":
    even_odd = ""
    if operator == "+":
        result = n1 + n2
    elif operator == "-":
        result = n1 - n2
    elif operator == "*":
        result = n1 * n2

    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"

    print(f"{n1} {operator} {n2} = {result} - {even_odd}")
elif operator == "/" or operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        if operator == "/":
            result = n1 / n2
            print(f"{n1} {operator} {n2} = {result:.2f}")
        else:
            result = n1 % n2
            print(f"{n1} {operator} {n2} = {result}")
