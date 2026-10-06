from lecture_9_modules.fibonacci_sequence.core import create_sequence, locate

command = input()
sequence = None

while command != "Stop":
    num = int(command.split()[-1])
    if command.startswith("Create"):
        sequence = create_sequence(num)
        print(*sequence)
    else:
        if sequence:
            print(locate(num, sequence))
        else:
            print("Please first initialise a sequence")

    command = input()