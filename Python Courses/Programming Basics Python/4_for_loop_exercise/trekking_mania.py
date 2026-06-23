groups_count = int(input())

v1 = 0
v2 = 0
v3 = 0
v4 = 0
v5 = 0

sum_of_people = 0

for i in range(groups_count):
    group_count = int(input())

    sum_of_people += group_count

    if group_count <= 5:
        v1 += group_count
    elif 6 <= group_count <= 12:
        v2 += group_count
    elif 13 <= group_count <= 25:
        v3 += group_count
    elif 26 <= group_count <= 40:
        v4 += group_count
    elif 41 <= group_count:
        v5 += group_count

v1_percent = (v1 / sum_of_people) * 100
v2_percent = (v2 / sum_of_people) * 100
v3_percent = (v3 / sum_of_people) * 100
v4_percent = (v4 / sum_of_people) * 100
v5_percent = (v5 / sum_of_people) * 100

print(f"{v1_percent:.2f}%")
print(f"{v2_percent:.2f}%")
print(f"{v3_percent:.2f}%")
print(f"{v4_percent:.2f}%")
print(f"{v5_percent:.2f}%")