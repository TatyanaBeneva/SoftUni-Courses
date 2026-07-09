sequences = input().split()
sums = []
uppercase_ord = ord('A') - 1
lowercase_ord = ord('a') - 1

for sequence in sequences:
    number = int(sequence[1:-1])
    total_sum = 0
    if sequence[0].isupper():
        total_sum += number / (ord(sequence[0]) - uppercase_ord)
    else:
        total_sum += number * (ord(sequence[0]) - lowercase_ord)

    if sequence[-1].isupper():
        total_sum -= ord(sequence[-1]) - uppercase_ord
    else:
        total_sum += ord(sequence[-1]) - lowercase_ord

    sums.append(total_sum)

print(f"{sum(sums):.2f}")