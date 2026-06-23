string_of_numbers = input()
numbers_to_remove = int(input())

numbers = list(map(int, string_of_numbers.split(" ")))

for _ in range(numbers_to_remove):
    index_of_the_smallest = numbers.index(min(numbers))
    numbers.pop(index_of_the_smallest)

print(", ".join(map(str, numbers)))