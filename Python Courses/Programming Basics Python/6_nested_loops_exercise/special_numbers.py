n = int(input())

for num in range(1111, 10000):
    char_count = len(str(num))
    counter = 0

    for index in range(char_count):
        current_digit = int(str(num)[index])

        if current_digit != 0 and  n % current_digit == 0:
            counter += 1
        else:
            break

    if counter == char_count:
        print(num, end=" ")