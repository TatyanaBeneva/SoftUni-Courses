n = int(input())
odd_set = set()
even_set = set()

for i in range(n):
    current_row = i + 1
    name = list(input())
    sum_of_chars = sum(ord(char) for char in name)
    result = int(sum_of_chars / current_row)

    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

sum_of_odd = sum(odd_set)
sum_of_even = sum(even_set)

if sum_of_odd == sum_of_even:
    print(*odd_set.union(even_set), sep=", ")
elif sum_of_odd > sum_of_even:
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")