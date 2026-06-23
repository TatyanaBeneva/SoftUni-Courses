width = int(input())
length = int(input())
height = int(input())
command = input()

available_space = width * length * height

while command != "Done":
    boxes_count = int(command)
    available_space -= boxes_count

    if available_space <= 0:
        print(f"No more free space! You need {abs(available_space)} Cubic meters more.")
        break

    command = input()

if command == "Done":
    print(f"{available_space} Cubic meters left.")