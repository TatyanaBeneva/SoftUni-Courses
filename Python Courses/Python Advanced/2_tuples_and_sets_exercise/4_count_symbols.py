text = list(input())
num_of_chars = {}

for i in range(len(text)):
    if text[i] not in num_of_chars:
        num_of_chars[text[i]] = 0

    num_of_chars[text[i]] += 1

for key, value in sorted(num_of_chars.items()):
    print(f"{key}: {value} time/s")