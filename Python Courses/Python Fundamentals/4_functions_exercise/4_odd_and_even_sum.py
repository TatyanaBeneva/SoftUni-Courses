def sum_of_even_odd_numbers(number: int):
    sum_of_even_numbers = 0
    sum_of_odd_numbers = 0

    for index in range(len(str(number))):
        n = int(str(number)[index])
        if n % 2 == 0:
            sum_of_even_numbers += n
        else:
            sum_of_odd_numbers += n

    return [sum_of_odd_numbers, sum_of_even_numbers]

number = int(input())
sum_of_odd_numbers, sum_of_even_numbers = sum_of_even_odd_numbers(number)
print(f"Odd sum = {sum_of_odd_numbers}, Even sum = {sum_of_even_numbers}")
