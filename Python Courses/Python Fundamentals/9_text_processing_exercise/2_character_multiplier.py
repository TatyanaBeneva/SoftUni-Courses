first_string, second_string = input().split()

total_sum = 0

min_length = min(len(first_string), len(second_string))

for index in range(min_length):
    total_sum += ord(first_string[index]) * ord(second_string[index])

if len(first_string) > len(second_string):
    for index in range(min_length, len(first_string)):
        total_sum += ord(first_string[index])
else:
    for index in range(min_length, len(second_string)):
        total_sum += ord(second_string[index])

print(total_sum)