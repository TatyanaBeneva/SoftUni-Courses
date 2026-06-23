low_score_count = int(input())
command = input()
score_sum = 0
score_count = 0
low_score_number = 0
last_problem = ""

while command != "Enough":
    name = command
    grade = int(input())
    score_sum += grade

    if grade <= 4:
        low_score_number += 1

        if low_score_number >= low_score_count:
            print(f"You need a break, {low_score_number} poor grades.")
            break

    score_count += 1
    last_problem = name
    command = input()
else:
    avg_score = score_sum / score_count

    print(f"Average score: {avg_score:.2f}")
    print(f"Number of problems: {score_count}")
    print(f"Last problem: {last_problem}")