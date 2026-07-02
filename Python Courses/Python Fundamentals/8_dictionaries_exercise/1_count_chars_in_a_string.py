word = input()
char_dict = {}

for char in word:
    if not char.isspace():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

for key, value in char_dict.items():
    print(f"{key} -> {value}")