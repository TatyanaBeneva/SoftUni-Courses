wagons = [0] * int(input())

while True:
    command = input().split()
    current_command = command[0]

    if current_command == 'add':
        number_of_people = int(command[1])
        wagons[-1] += number_of_people
    elif current_command == 'insert':
        index = int(command[1])
        people = int(command[2])
        wagons[index] += people
    elif current_command == 'leave':
        index = int(command[1])
        people = int(command[2])
        wagons[index] -= people
    elif current_command == "End":
        print(wagons)
        break