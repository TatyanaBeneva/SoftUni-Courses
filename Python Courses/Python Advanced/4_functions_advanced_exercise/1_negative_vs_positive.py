numbers = [int(el) for el in input().split()]

negative_numbers = [el for el in numbers if el < 0]
positive_numbers = [el for el in numbers if el > 0]
negative_numbers_sum = sum(negative_numbers)
positive_numbers_sum = sum(positive_numbers)
is_negative_numbers_stronger = abs(negative_numbers_sum) > positive_numbers_sum

print(negative_numbers_sum)
print(positive_numbers_sum)

if is_negative_numbers_stronger:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")