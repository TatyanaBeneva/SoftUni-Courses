def calc_sum(numbers, index):
    if index == len(numbers) - 1:
        return numbers[index]

    return numbers[index] + calc_sum(numbers, index + 1)

nums = [int(n) for n in input().split()]

print(calc_sum(nums, 0))