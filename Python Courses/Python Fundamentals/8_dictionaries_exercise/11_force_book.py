def main():
    forced_users = {}

    while True:
        data = input()

        if data == "Lumpawaroo":
            break

        if "|" in data:
            force_side, force_user = data.split(" | ")

            if not is_force_user(force_user, forced_users):
                forced_users = add_user_to_side(force_user, force_side, forced_users)
            else:
                continue
        else:
            force_user, force_side = data.split(" -> ")

            if is_force_user(force_user, forced_users):
                forced_users = remove_user(force_user, forced_users)
                forced_users = add_user_to_side(force_user, force_side, forced_users)
            elif not is_force_user(force_user, forced_users):
                forced_users = add_user_to_side(force_user, force_side, forced_users)

            print(f"{force_user} joins the {force_side} side!")

    forced_users = {k: v for k, v in forced_users.items() if len(v) > 0}

    for key, values in forced_users.items():
        print(f"Side: {key}, Members: {len(values)}")

        for value in values:
            print(f"! {value}")

def is_force_user(user: str, dictionary: dict) -> bool:
    return any(user in v for v in dictionary.values())

def add_user_to_side(user: str, side: str, dictionary: dict) -> dict:
    if side not in dictionary:
        dictionary[side] = [user]
    else:
        dictionary[side].append(user)

    return dictionary

def remove_user(user, dictionary: dict) -> dict:
    for value_list in dictionary.values():
        if user in value_list:
            value_list.remove(user)
            break

    return dictionary

main()