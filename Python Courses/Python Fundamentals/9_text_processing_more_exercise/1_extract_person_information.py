n = int(input())

for _ in range(n):
    text = input()

    name_start_index = text.index("@") + 1
    name_end_index = text.index("|")
    age_start_index = text.index("#") + 1
    age_end_index = text.index("*")
    name = text[name_start_index:name_end_index]
    age = text[age_start_index:age_end_index]

    print(f"{name} is {age} years old.")