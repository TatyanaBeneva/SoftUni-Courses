from math import ceil

persons = int(input())
capacity = int(input())
# counter = 0
#
# for i in range(1, persons + 1, capacity):
#     counter += 1
#
# print(counter)

courses = ceil(persons / capacity)
print(courses)