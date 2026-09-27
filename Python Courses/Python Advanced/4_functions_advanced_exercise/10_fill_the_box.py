from collections import deque

def fill_the_box(height, length, width, *args):
    remaining_space = height * length * width

    for cubes in args:
        if cubes == "Finish":
            break
        remaining_space -= cubes

    if remaining_space > 0:
        return (
            f"There is free space in the box. "
            f"You could put {remaining_space} more cubes."
        )

    return (
        f"No more free space! "
        f"You have {-remaining_space} more cubes."
    )




print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))