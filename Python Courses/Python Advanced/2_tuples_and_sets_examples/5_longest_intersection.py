n = int(input())
longest_intersection = []

for _ in range(n):
    text = input().split("-")
    first_start, first_end = map(int, text[0].split(","))
    second_start, second_end = map(int, text[1].split(","))
    first_set = set()
    second_set = set()

    for i in range(first_start, first_end+1):
        first_set.add(i)

    for i in range(second_start, second_end+1):
        second_set.add(i)

    intersection = first_set.intersection(second_set)

    if len(intersection) > len(longest_intersection):
        longest_intersection = list(intersection)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")

