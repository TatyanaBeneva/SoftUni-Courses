from string import punctuation

result = []

with open("text.txt") as file:
    for index, line in enumerate(file):
        letters_count = sum(1 for char in line if char.isalpha())
        punctuations_count = sum(1 for char in line if char in punctuation)
        result.append(f"Line {index+1}: {line} ({letters_count})({punctuations_count})")

with open("output.txt", "w") as file:
    for line in result:
        file.write(f"{line}\n")