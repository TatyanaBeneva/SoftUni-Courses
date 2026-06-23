string_numbers_list = input().split(", ")
numbers_list = list(map(int, string_numbers_list))

for number in numbers_list:
    if number == 0:
        numbers_list.remove(0)
        numbers_list.append(0)

print(numbers_list)