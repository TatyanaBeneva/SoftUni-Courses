n = int(input())
students = {}

for _ in range(n):
    student = input()
    grade = float(input())

    if student in students:
        students[student].append(grade)
    else:
        students[student] = [grade]

students = {key: value for key, value in students.items() if (sum(value) / len(value)) >= 4.50}

for key, value in students.items():
    average_grade = (sum(value) / len(value))
    print(f"{key} -> {average_grade:.2f}")
