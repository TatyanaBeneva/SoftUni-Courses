def fibonaci_numbers(n: int):
    numbers = []
    for i in range(n):
        if i < 2:
            numbers.append(1)
        else:
            summ = 0
            if i == 2:
                summ = 0 + numbers[0] + numbers[1]
            else:
                summ = numbers[i - 1] + numbers[i - 2] + numbers[i - 3]

            numbers.append(summ)

    return numbers

number = int(input())
numbers = fibonaci_numbers(number)
print(" ".join(map(str, numbers)))