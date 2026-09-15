expression = input().split()
operators = {"+", "-", "*", "/"}
numbers = []

for token in expression:
    if token not in operators:
        numbers.append(int(token))
        continue

    result = numbers[0]

    for number in numbers[1:]:
        match token:
            case "+":
                result += number
            case "-":
                result -= number
            case "*":
                result *= number
            case "/":
                result = int(result / number)

    numbers = [result]

print(numbers[0])