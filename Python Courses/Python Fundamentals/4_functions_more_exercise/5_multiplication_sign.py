def is_positive(n1, n2, n3):
    if n1 == 0 or n2 == 0 or n3 == 0:
        return "zero"

    counter_of_negative_number = 0

    if n1 < 0:
        counter_of_negative_number += 1
    if n2 < 0:
        counter_of_negative_number += 1
    if n3 < 0:
        counter_of_negative_number += 1

    if counter_of_negative_number % 2 != 0:
        return "negative"
    else:
        return "positive"

n1 = int(input())
n2 = int(input())
n3 = int(input())

print(is_positive(n1, n2, n3))