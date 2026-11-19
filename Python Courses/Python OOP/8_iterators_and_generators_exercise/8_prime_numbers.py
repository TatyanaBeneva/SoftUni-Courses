def get_primes(list_num):
    for num in list_num:
        if num < 2:
            continue

        is_prime = True
        for divisor in range(2, num):
            if num % divisor == 0:
                is_prime = False
                break

        if is_prime:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
