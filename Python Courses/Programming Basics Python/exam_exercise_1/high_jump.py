needed_height = int(input())
current_height = needed_height - 30
all_jumps = 0

while current_height <= needed_height:
    is_jump_successful = False
    jump_counter = 0

    for jump in range(1, 4):
        height = int(input())
        all_jumps += 1

        if height > current_height:
            is_jump_successful = True
            current_height += 5
            break
        else:
            jump_counter += 1

    if not is_jump_successful:
        print(f"Tihomir failed at {current_height}cm after {all_jumps} jumps.")
        break

if current_height > needed_height:
    print(f"Tihomir succeeded, he jumped over {current_height - 5}cm after {all_jumps} jumps.")