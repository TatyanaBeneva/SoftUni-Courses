substrings = input().split()

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}
all_colors = main_colors.union(secondary_colors)

found_colors = []

while substrings:
    first = substrings.pop(0)

    if substrings:
        last = substrings.pop()
    else:
        last = ""

    first_last = first + last
    last_first = last + first

    if first_last in all_colors:
        found_colors.append(first_last)

    elif last_first in all_colors:
        found_colors.append(last_first)

    else:
        first = first[:-1]
        last = last[:-1]

        middle = len(substrings) // 2

        if first:
            substrings.insert(middle, first)
            middle += 1

        if last:
            substrings.insert(middle, last)

secondary_requirements = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

result = []

for color in found_colors:
    if color in main_colors:
        result.append(color)
    elif secondary_requirements[color].issubset(found_colors):
        result.append(color)

print(result)