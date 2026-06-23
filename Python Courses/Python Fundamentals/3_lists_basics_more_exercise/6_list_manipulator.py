numbers = list(map(int, input().split()))

command = input()

while command != "end":
    command_parts = command.split()
    action = command_parts[0]

    if action == "exchange":
        index = int(command_parts[1])

        if index < 0 or index >= len(numbers):
            print("Invalid index")
        else:
            left_part = numbers[:index + 1]
            right_part = numbers[index + 1:]
            numbers = right_part + left_part

    elif action == "max" or action == "min":
        number_type = command_parts[1]

        best_number = None
        best_index = -1

        for index in range(len(numbers)):
            current_number = numbers[index]

            if number_type == "even" and current_number % 2 != 0:
                continue

            if number_type == "odd" and current_number % 2 == 0:
                continue

            if best_number is None:
                best_number = current_number
                best_index = index
            else:
                if action == "max":
                    if current_number >= best_number:
                        best_number = current_number
                        best_index = index
                elif action == "min":
                    if current_number <= best_number:
                        best_number = current_number
                        best_index = index

        if best_index == -1:
            print("No matches")
        else:
            print(best_index)

    elif action == "first" or action == "last":
        count = int(command_parts[1])
        number_type = command_parts[2]

        if count > len(numbers):
            print("Invalid count")
        else:
            filtered_numbers = []

            for number in numbers:
                if number_type == "even" and number % 2 == 0:
                    filtered_numbers.append(number)
                elif number_type == "odd" and number % 2 != 0:
                    filtered_numbers.append(number)

            if action == "first":
                print(filtered_numbers[:count])
            elif action == "last":
                print(filtered_numbers[-count:])

    command = input()

print(numbers)