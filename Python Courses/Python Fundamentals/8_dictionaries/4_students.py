def main():
    students = []

    while True:
        student_data = input()

        if student_data.islower():
            check_course(student_data, students)
            break

        student_name, student_id, course = student_data.split(":")
        students.append({
            "name": student_name,
            "id": student_id,
            "course": course
        })

def check_course(data: str, students_list: list):
    course_data = data.replace("_", " ")
    for student in students_list:
        if student["course"] == course_data:
            print(f"{student['name']} - {student['id']}")

main()