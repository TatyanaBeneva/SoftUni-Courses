def main():
    dwarfs = read_dwarfs()
    print_dwarfs(dwarfs)


def read_dwarfs() -> dict:
    dwarfs = {}

    while True:
        command = input()

        if command == "Once upon a time":
            break

        name, hat_color, physics = command.split(" <:> ")
        physics = int(physics)

        dwarf_key = (name, hat_color)

        if dwarf_key not in dwarfs:
            dwarfs[dwarf_key] = physics
        elif dwarfs[dwarf_key] < physics:
            dwarfs[dwarf_key] = physics

    return dwarfs


def get_hat_color_counts(dwarfs: dict) -> dict:
    hat_color_counts = {}

    for name, hat_color in dwarfs:
        if hat_color not in hat_color_counts:
            hat_color_counts[hat_color] = 0

        hat_color_counts[hat_color] += 1

    return hat_color_counts


def print_dwarfs(dwarfs: dict):
    hat_color_counts = get_hat_color_counts(dwarfs)

    sorted_dwarfs = sorted(
        dwarfs.items(),
        key=lambda item: (
            -item[1],
            -hat_color_counts[item[0][1]]
        )
    )

    for dwarf, physics in sorted_dwarfs:
        name, hat_color = dwarf

        print(f"({hat_color}) {name} <-> {physics}")


main()