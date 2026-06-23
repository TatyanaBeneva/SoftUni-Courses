numbers_string = input().split(" ")
magic_number = int(input())

numbers_list = list(map(int, numbers_string))
result = []
index = 0

while len(numbers_list) > 0:
    index = (index + magic_number - 1) % len(numbers_list)

    result.append(numbers_list[index])
    numbers_list.pop(index)

print(str(result).replace(" ", ""))
