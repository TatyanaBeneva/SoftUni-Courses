shopping_list = input().split("!")
command = input()

while command != "Go Shopping!":
    command_list = command.split()
    current_command = command_list[0]
    item = command_list[1]

    if current_command == "Urgent" and item not in shopping_list:
        shopping_list.insert(0, item)

    elif current_command == "Unnecessary" and item in shopping_list:
        shopping_list.remove(item)

    elif current_command == "Correct" and item in shopping_list:
        new_item = command_list[2]
        item_index = shopping_list.index(item)
        shopping_list[item_index] = new_item

    elif current_command == "Rearrange" and item in shopping_list:
        shopping_list.remove(item)
        shopping_list.append(item)

    command = input()

print(", ".join(shopping_list))
