upper_limit_first_num = int(input())
upper_limit_second_num = int(input())
upper_limit_third_num = int(input())

for n1 in range(2, upper_limit_first_num + 1):
    for n2 in range(2, upper_limit_second_num + 1):
        for n3 in range(2, upper_limit_third_num + 1):

            if n1 % 2 == 0 and \
               (n2 == 2 or n2 == 3 or n2 == 5 or n2 == 7) and \
               n3 % 2 == 0:

                print(f"{n1} {n2} {n3}")