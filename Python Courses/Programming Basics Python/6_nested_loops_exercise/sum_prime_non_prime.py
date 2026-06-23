prime_sum = 0
non_prime_sum = 0

while True:
    number = input()
    is_prime = True

    if number == "stop":
        break

    number = int(number)

    if number < 0:
        print("Number is negative.")
        continue

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_sum += number
    else:
        non_prime_sum += number

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")