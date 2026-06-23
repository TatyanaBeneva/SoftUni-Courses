students_count = int(input())

grades_sum = 0.0
grade_two_count = 0
grade_three_count = 0
grade_four_count = 0
grade_five_count = 0

for student in range(1, students_count+1):
    grade = float(input())

    if 2 <= grade < 3:
        grade_two_count += 1
    elif 3 <= grade < 4:
        grade_three_count += 1
    elif 4 <= grade < 5:
        grade_four_count += 1
    elif 5 <= grade <= 6:
        grade_five_count += 1

    grades_sum += grade

print(f"Top students: {grade_five_count / students_count * 100:.2f}%")
print(f"Between 4.00 and 4.99: {grade_four_count / students_count * 100:.2f}%")
print(f"Between 3.00 and 3.99: {grade_three_count / students_count * 100:.2f}%")
print(f"Fail: {grade_two_count / students_count * 100:.2f}%")
print(f"Average: {grades_sum / students_count:.2f}")