courses = input().split(", ")

while True:
    command = input()

    if command == "course start":
        break

    command_parts = command.split(":")
    action = command_parts[0]
    lesson = command_parts[1]
    exercise = f"{lesson}-Exercise"

    if action == "Add":
        if lesson not in courses:
            courses.append(lesson)

    elif action == "Insert":
        index = int(command_parts[2])

        if lesson not in courses:
            courses.insert(index, lesson)

    elif action == "Remove":
        if lesson in courses:
            lesson_index = courses.index(lesson)
            courses.pop(lesson_index)

            if (
                lesson_index < len(courses)
                and courses[lesson_index] == exercise
            ):
                courses.pop(lesson_index)

    elif action == "Swap":
        second_lesson = command_parts[2]
        second_exercise = f"{second_lesson}-Exercise"

        if lesson in courses and second_lesson in courses:
            first_index = courses.index(lesson)
            second_index = courses.index(second_lesson)

            courses[first_index], courses[second_index] = \
                courses[second_index], courses[first_index]

            if exercise in courses:
                courses.remove(exercise)
                new_lesson_index = courses.index(lesson)
                courses.insert(new_lesson_index + 1, exercise)

            if second_exercise in courses:
                courses.remove(second_exercise)
                new_second_lesson_index = courses.index(second_lesson)
                courses.insert(
                    new_second_lesson_index + 1,
                    second_exercise,
                )

    elif action == "Exercise":
        if lesson in courses:
            if exercise not in courses:
                lesson_index = courses.index(lesson)
                courses.insert(lesson_index + 1, exercise)
        else:
            courses.extend([lesson, exercise])

for index, course in enumerate(courses, start=1):
    print(f"{index}.{course}")