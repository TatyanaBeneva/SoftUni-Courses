keys = list(map(int, input().split()))

while True:
    string = input()

    if string == "find":
        break

    new_string = ""
    i = 0

    for char in string:
        if i > len(keys) - 1:
            i = 0

        new_string += chr(ord(char) - keys[i])
        i += 1

    type_start_index = new_string.index("&") + 1
    type_end_index = new_string.index("&", type_start_index)
    coordinates_start_index = new_string.index("<") + 1
    coordinates_end_index = new_string.index(">")
    treasure_type = new_string[type_start_index:type_end_index]
    coordinates = new_string[coordinates_start_index:coordinates_end_index]

    print(f"Found {treasure_type} at {coordinates}")