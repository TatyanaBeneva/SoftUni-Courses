word = input()
list_of_uppercase_letters = []

for index in range(len(word)):
    if word[index].isupper():
        list_of_uppercase_letters.append(index)

print(list_of_uppercase_letters)