factor = int(input())
count = int(input())

array_of_numbers = []
factor_counter = factor

for _ in range(count):
    array_of_numbers.append(factor_counter)
    factor_counter += factor

print(array_of_numbers)