numbers_as_strings = input().split(", ")
beggars_count = int(input())

numbers = [int(number) for number in numbers_as_strings]

result = []

for beggar_index in range(beggars_count):
    current_sum = 0

    for index in range(beggar_index, len(numbers), beggars_count):
        current_sum += numbers[index]

    result.append(current_sum)

print(result)