num = int(input())
numbers = []
largest_number = ""

for n in str(num):
    numbers.append(int(n))

numbers.sort(reverse=True)

for index in range(len(str(num))):
    largest_number += str(numbers[index])

print(int(largest_number))

# num = input()
#
# largest_number = sorted(num, reverse=True)
#
# print(int("".join(largest_number)))