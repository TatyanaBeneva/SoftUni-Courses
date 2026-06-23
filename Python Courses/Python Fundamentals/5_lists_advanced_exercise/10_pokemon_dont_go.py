distances_to_pokemon = list(map(int, input().split()))
sum_of_removed_elements = 0

while distances_to_pokemon:
    index = int(input())

    if index < 0:
        removed_element = distances_to_pokemon[0]
        distances_to_pokemon[0] = distances_to_pokemon[-1]

    elif index >= len(distances_to_pokemon):
        removed_element = distances_to_pokemon[-1]
        distances_to_pokemon[-1] = distances_to_pokemon[0]

    else:
        removed_element = distances_to_pokemon.pop(index)

    sum_of_removed_elements += removed_element

    distances_to_pokemon = [
        pokemon + removed_element
        if pokemon <= removed_element
        else pokemon - removed_element
        for pokemon in distances_to_pokemon
    ]

print(sum_of_removed_elements)