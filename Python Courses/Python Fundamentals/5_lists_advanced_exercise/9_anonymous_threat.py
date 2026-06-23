words = input().split()
command = input()

while command != "3:1":
    command_list = command.split()
    current_command = command_list[0]
    start_index = int(command_list[1])
    end_index = int(command_list[2])

    if current_command == "merge":
        if end_index >= len(words):
            end_index = len(words)-1

        if start_index < 0:
            start_index = 0

        word = ""

        for i in range(end_index - start_index + 1):
            word += words.pop(start_index)

        words.insert(start_index, word)

    elif current_command == "divide":
        word_to_divide = words.pop(start_index)
        partition_length = len(word_to_divide) // end_index
        current_index = start_index
        start = 0

        for partition in range(end_index):
            if partition == end_index - 1:
                divided_part = word_to_divide[start:]
            else:
                divided_part = word_to_divide[start:start + partition_length]

            words.insert(current_index, divided_part)

            current_index += 1
            start += partition_length

    command = input()

print(" ".join(words))