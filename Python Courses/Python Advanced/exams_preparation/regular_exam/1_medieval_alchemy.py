from collections import deque

def main():
    potions = {
        "Brew of Immortality": 110,
        "Essence of Resilience": 100,
        "Draught of Wisdom": 90,
        "Potion of Agility": 80,
        "Elixir of Strength": 70
    }

    substances = [int(el) for el in input().split(", ")]
    crystals_energy_levels = deque(int(el) for el in input().split(", "))

    crafted_potions = []

    while (len(crafted_potions) < len(potions)) and substances and crystals_energy_levels:
        current_substance = substances.pop()
        current_crystal_level = crystals_energy_levels.popleft()
        energy_sum = current_crystal_level + current_substance

        for potion, level in potions.items():
            if potion in crafted_potions:
                continue

            if energy_sum >= level:
                crafted_potions.append(potion)

                if energy_sum == level:
                    current_crystal_level = 0
                else:
                    current_crystal_level -= 20

                break
        else:
            current_crystal_level -= 5

        if current_crystal_level > 0:
            crystals_energy_levels.append(current_crystal_level)

    print(app_result(crafted_potions, potions, substances, crystals_energy_levels))


def app_result(crafted_potions, potions, substances, crystals_energy_levels):
    result = []
    if len(crafted_potions) == len(potions):
        result.append("Success! The alchemist has forged all potions!")
    else:
        result.append("The alchemist failed to complete his quest.")

    if crafted_potions:
        result.append(f"Crafted potions: {', '.join(crafted_potions)}")

    if substances:
        result.append(f"Substances: {', '.join(map(str, reversed(substances)))}")

    if crystals_energy_levels:
        result.append(f"Crystals: {', '.join(map(str, crystals_energy_levels))}")

    return "\n".join(result)


if __name__ == "__main__":
    main()