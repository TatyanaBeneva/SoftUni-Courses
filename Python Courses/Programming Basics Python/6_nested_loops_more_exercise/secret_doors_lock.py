hundreds_limit = int(input())
tens_limit = int(input())
units_limit = int(input())

for h in range(2, hundreds_limit + 1):
    for t in range(2, tens_limit + 1):
        for u in range(2, units_limit + 1):

            is_t_prime = t == 2 or t == 3 or t == 5 or t == 7

            if h % 2 == 0 and u % 2 == 0 and is_t_prime:
                print(f"{h} {t} {u}")