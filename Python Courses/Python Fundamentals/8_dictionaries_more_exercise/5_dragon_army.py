def main():
    dragons = read_dragons()
    print_dragons(dragons)


def get_stat(value: str, default_value: int) -> int:
    if value == "null":
        return default_value

    return int(value)


def read_dragons() -> dict:
    dragons = {}

    number_of_dragons = int(input())

    for _ in range(number_of_dragons):
        dragon_type, name, damage, health, armor = input().split()

        damage = get_stat(damage, 45)
        health = get_stat(health, 250)
        armor = get_stat(armor, 10)

        if dragon_type not in dragons:
            dragons[dragon_type] = {}

        dragons[dragon_type][name] = {
            "damage": damage,
            "health": health,
            "armor": armor
        }

    return dragons


def print_dragons(dragons: dict):
    for dragon_type, dragons_by_name in dragons.items():
        total_damage = 0
        total_health = 0
        total_armor = 0

        for stats in dragons_by_name.values():
            total_damage += stats["damage"]
            total_health += stats["health"]
            total_armor += stats["armor"]

        dragons_count = len(dragons_by_name)

        average_damage = total_damage / dragons_count
        average_health = total_health / dragons_count
        average_armor = total_armor / dragons_count

        print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")

        sorted_dragons = sorted(dragons_by_name.items())

        for dragon_name, stats in sorted_dragons:
            print(
                f"-{dragon_name} -> "
                f"damage: {stats['damage']}, "
                f"health: {stats['health']}, "
                f"armor: {stats['armor']}"
            )


main()