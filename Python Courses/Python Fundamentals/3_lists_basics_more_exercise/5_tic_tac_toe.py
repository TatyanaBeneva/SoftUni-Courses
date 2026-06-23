first_line = input().split(" ")
second_line = input().split(" ")
third_line = input().split(" ")

result = "Draw!"

if first_line[0] == first_line[1] == first_line[2] or\
        first_line[0] == second_line[0] == third_line[0] or\
        first_line[0] == second_line[1] == third_line[2]:
    if first_line[0] == "1":
        result = "First player won"
    elif first_line[0] == "2":
        result = "Second player won"
elif second_line[0] == second_line[1] == second_line[2]:
    if second_line[0] == "1":
        result = "First player won"
    elif second_line[0] == "2":
        result = "Second player won"
elif third_line[0] == third_line[1] == third_line[2]:
    if third_line[0] == "1":
        result = "First player won"
    elif third_line[0] == "2":
        result = "Second player won"
elif first_line[1] == second_line[1] == third_line[1]:
    if first_line[1] == "1":
        result = "First player won"
    elif first_line[1] == "2":
        result = "Second player won"
elif first_line[2] == second_line[2] == third_line[2] or\
        first_line[2] == second_line[1] == third_line[0]:
    if first_line[2] == "1":
        result = "First player won"
    elif first_line[2] == "2":
        result = "Second player won"

print(result)