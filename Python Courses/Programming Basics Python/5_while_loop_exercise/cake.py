width = int(input())
height = int(input())

cake_pieces = width * height

while True:
    command = input()

    if command == "STOP":
        print(f"{cake_pieces} pieces are left.")
        break

    taken_pieces = int(command)
    cake_pieces -= taken_pieces

    if cake_pieces <= 0:
        print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
        break