names_list = input().split(", ")
names_sorted_descending = sorted(names_list, key=lambda name: (-len(name), name))

print(names_sorted_descending)