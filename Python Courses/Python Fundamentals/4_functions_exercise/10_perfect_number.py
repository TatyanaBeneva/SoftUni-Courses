def is_the_number_perfect(number: int):
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == number:
        return True
    else:
        return False

number = int(input())
is_number_perfect = is_the_number_perfect(number)

if is_number_perfect:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")