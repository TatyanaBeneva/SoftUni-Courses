n = int(input())
word = input()
all_strings_list = []
filtered_list = []

for i in range(n):
    current_string = input()
    all_strings_list.append(current_string)

for string in all_strings_list:
    if word in string:
        filtered_list.append(string)


print(all_strings_list)
print(filtered_list)