exam_results = {}
submissions = {}

while True:
    data = input()

    if data == "exam finished":
        break

    command = data.split("-")
    username = command[0]

    if command[1] == "banned":
        if username in exam_results:
            del exam_results[username]
        continue

    language = command[1]
    points = int(command[2])

    if language not in submissions:
        submissions[language] = 0
    submissions[language] += 1

    if username not in exam_results:
        exam_results[username] = points
    else:
        if points > exam_results[username]:
            exam_results[username] = points

print("Results:")
for username, points in exam_results.items():
    print(f"{username} | {points}")

print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")