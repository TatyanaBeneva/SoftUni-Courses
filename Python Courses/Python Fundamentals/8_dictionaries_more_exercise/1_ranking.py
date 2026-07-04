def main():
    contests = read_contests()
    submissions = read_submissions(contests)
    print(submissions)

    print_best_candidate(submissions)
    print_ranking(submissions)

def read_contests():
    contests = {}

    while True:
        command = input()

        if command == "end of contests":
            break

        contest, password = command.split(":")
        contests[contest] = password

    return contests


def read_submissions(contests):
    submissions = {}

    while True:
        command = input()

        if command == "end of submissions":
            break

        contest, password, username, points = command.split("=>")
        points = int(points)

        if contest not in contests or contests[contest] != password:
            continue

        if username not in submissions:
            submissions[username] = {}

        if contest not in submissions[username]:
            submissions[username][contest] = points
        elif points > submissions[username][contest]:
            submissions[username][contest] = points

    return submissions


def get_total_points(user_contests):
    return sum(user_contests.values())


def print_best_candidate(submissions):
    best_username = ""
    best_points = 0

    for username, contests in submissions.items():
        total_points = get_total_points(contests)

        if total_points > best_points:
            best_username = username
            best_points = total_points

    print(f"Best candidate is {best_username} with total {best_points} points.")


def print_ranking(submissions):
    print("Ranking:")

    for username, contests in sorted(submissions.items()):
        print(username)

        sorted_contests = sorted(
            contests.items(),
            key=lambda contest: contest[1],
            reverse=True
        )

        for contest, points in sorted_contests:
            print(f"#  {contest} -> {points}")

main()