def main():
    followers = []

    while True:
        command = input()

        if command == "Log out":
            break

        command = command.split(": ")
        action = command[0]
        username = command[1]

        if action == "New follower":
            if not is_user_exist(username, followers):
                followers.append({"username": username, "likes": 0, "comments": 0})

        elif action == "Like":
            count = int(command[2])

            if is_user_exist(username, followers):
                for follower in followers:
                    if follower["username"] == username:
                        follower["likes"] += count
                        break
            else:
                followers.append({"username": username, "likes": count, "comments": 0})

        elif action == "Comment":
            if is_user_exist(username, followers):
                for follower in followers:
                    if follower["username"] == username:
                        follower["comments"] += 1
                        break
            else:
                followers.append({"username": username, "likes": 0, "comments": 1})
        elif action == "Blocked":
            if not is_user_exist(username, followers):
                print(f"{username} doesn't exist.")
            else:
                followers = [
                    follower for follower in followers
                    if follower["username"] != username
                ]

    print_result(followers)


def is_user_exist(username: str, followers: list) -> bool:
    return any(follower["username"] == username for follower in followers)


def print_result(followers: list) -> None:
    print(f"{len(followers)} followers")

    for follower in followers:
        print(f"{follower['username']}: {follower['likes'] + follower['comments']}")


main()