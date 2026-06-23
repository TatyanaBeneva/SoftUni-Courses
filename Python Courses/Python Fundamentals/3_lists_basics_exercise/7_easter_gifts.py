gifts = input()
command = input()
gifts_array = gifts.split(" ")

while command != "No Money":
    array = command.split(" ")
    current_command = array[0]
    current_gift = array[1]

    if current_command == "OutOfStock":
        for index in range(len(gifts_array)):
            if gifts_array[index] == current_gift:
                gifts_array[index] = "None"
    elif current_command == "Required":
        index = int(array[2])

        if 0 <= index < len(gifts_array):
            gifts_array[index] = current_gift
    elif current_command == "JustInCase":
        gifts_array[-1] = current_gift

    command = input()

gifts_array = list(filter(lambda gift: gift != "None", gifts_array))
print(" ".join(gifts_array))
