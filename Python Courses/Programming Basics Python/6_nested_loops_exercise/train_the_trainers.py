jury_count = int(input())
all_grades_sum = 0
grades_count = 0

while True:
    presentation_name = input()

    if presentation_name == "Finish":
        break

    sum_presentation_grade = 0

    for i in range(jury_count):
        grade = float(input())
        sum_presentation_grade += grade
        grades_count += 1

    all_grades_sum += sum_presentation_grade
    average_presentation_grade = sum_presentation_grade / jury_count
    print(f"{presentation_name} - {average_presentation_grade:.2f}.")

average_student_grade = all_grades_sum / grades_count
print(f"Student's final assessment is {average_student_grade:.2f}.")