n = int(input())
is_prime = True

for divisor in range(2, n):
    if n % divisor == 0:
        is_prime = False
        break

print(is_prime)