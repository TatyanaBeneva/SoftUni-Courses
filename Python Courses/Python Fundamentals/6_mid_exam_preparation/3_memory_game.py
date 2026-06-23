def is_invalid(index1, index2, elements) -> bool:
    if (0 > index1 or index1 >= len(elements)
            or 0 > index2 or index2 >= len(elements)
         or index1 == index2):
        mid_index = len(elements) // 2
        elements.insert(mid_index, f"-{moves}a")
        elements.insert(mid_index + 1, f"-{moves}a")
        # first_part = elements[:mid_index]
        # second_part = elements[mid_index:]
        # elements = first_part + [f"-{moves}a"] + [f"-{moves}a"] + second_part
        return True

    return False

sequence_of_elements = input().split()
moves = 0
is_player_won = False

while True:
    command = input()

    if command == "end":
        break

    moves += 1

    index_1, index_2 = list(map(int, command.split()))

    if is_invalid(index_1, index_2, sequence_of_elements):
        print("Invalid input! Adding additional elements to the board")
        continue

    if sequence_of_elements[index_1] == sequence_of_elements[index_2]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[index_1]}!")
        sequence_of_elements.pop(max(index_1, index_2))
        sequence_of_elements.pop(min(index_1, index_2))
    elif sequence_of_elements[index_1] != sequence_of_elements[index_2]:
        print("Try again!")

    if len(sequence_of_elements) == 0:
        is_player_won = True
        break

if is_player_won:
    print(f"You have won in {moves} turns!")
else:
    print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)}")