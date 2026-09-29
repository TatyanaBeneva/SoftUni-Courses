import re

with open("words.txt") as file:
    words = file.read().split()

with open("input.txt") as file:
    text = file.read()

data = {}

for word in words:
    pattern = rf"\b{word}\b"
    matches = re.findall(pattern, text, re.IGNORECASE)
    data[word] = len(matches)

ordered_data = sorted(data.items(), key=lambda x: -x[1])

with open("output.txt", "w") as file:
    for word, count in ordered_data:
        file.write(f"{word} - {count}\n")