def main():
    contests = read_submissions()

    print_contests(contests)
    print_individual_standings(contests)

def read_submissions():
    contests = {}

    while True:
        command = input()

        if command == "no more time":
            break

        username, contest, points = command.split(" -> ")
        points = int(points)

        if contest not in contests:
            contests[contest] = {}

        if username not in contests[contest]:
            contests[contest][username] = points
        elif points > contests[contest][username]:
            contests[contest][username] = points

    return contests


def get_users_total_points(contests):
    users_total_points = {}

    for users in contests.values():
        for username, points in users.items():
            if username not in users_total_points:
                users_total_points[username] = 0

            users_total_points[username] += points

    return users_total_points


def print_contests(contests):
    for contest, users in contests.items():
        print(f"{contest}: {len(users)} participants")

        sorted_users = sorted(
            users.items(),
            key=lambda item: (-item[1], item[0])
        )

        for index, (username, points) in enumerate(sorted_users, start=1):
            print(f"{index}. {username} <::> {points}")


def print_individual_standings(contests):
    users_total_points = get_users_total_points(contests)

    sorted_users = sorted(
        users_total_points.items(),
        key=lambda item: (-item[1], item[0])
    )

    print("Individual standings:")

    for index, (username, points) in enumerate(sorted_users, start=1):
        print(f"{index}. {username} -> {points}")

main()