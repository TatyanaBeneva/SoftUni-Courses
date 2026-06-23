first_start = int(input())
second_start = int(input())
first_diff = int(input())
second_diff = int(input())

first_end = first_start + first_diff
second_end = second_start + second_diff

for first_pair in range(first_start, first_end + 1):
    for second_pair in range(second_start, second_end + 1):

        first_is_prime = True
        second_is_prime = True

        for i in range(2, first_pair):
            if first_pair % i == 0:
                first_is_prime = False
                break

        for i in range(2, second_pair):
            if second_pair % i == 0:
                second_is_prime = False
                break

        if first_is_prime and second_is_prime:
            print(f"{first_pair}{second_pair}")