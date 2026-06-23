def plant_crop(crop: str, crop_list: list) -> list:
    if crop not in crop_list:
        crop_list.insert(0, crop)

    return crop_list

def transplant_crop(crop: str, crop_list: list) -> list:
    if crop in crop_list:
        crop_list.remove(crop)
        crop_list.append(crop)

    return crop_list

def replace_crop(first_index: int, second_index: int, crop_list: list) -> list:
    if 0 <= first_index < len(crop_list) and 0 <= second_index < len(crop_list):
        crop_list[first_index], crop_list[second_index] =\
            crop_list[second_index], crop_list[first_index]

    return  crop_list

def uproot_crop(crop: str, crop_list: list) -> list:
    if crop in crop_list:
        crop_list.remove(crop)

    return crop_list

crops = input().split(" & ")

while True:
    command = input()

    if command == "Collect!":
        break

    command_list = command.split()
    action = command_list[0]

    if action == "Plant":
        crops = plant_crop(command_list[1], crops)
    elif action == "Transplant":
        crops = transplant_crop(command_list[1], crops)
    elif action == "Replace":
        crops = replace_crop(int(command_list[1]), int(command_list[2]), crops)
    elif action == "Uproot":
        crops = uproot_crop(command_list[1], crops)

print(" | ".join(crops))