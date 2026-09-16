from collections import deque

boxes = list(map(int, input().split()))
magic_numbers = deque(map(int, input().split()))
materials = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
presents = {}

while boxes and magic_numbers:
    box = boxes[-1]
    magic = magic_numbers[0]

    if box == 0 or magic == 0:
        if box == 0:
            boxes.pop()

        if magic == 0:
            magic_numbers.popleft()

        continue

    total_magic_level = box * magic

    if total_magic_level in materials:
        present = materials[total_magic_level]

        if present not in presents:
            presents[present] = 0

        presents[present] += 1
        boxes.pop()
        magic_numbers.popleft()
        continue

    if total_magic_level < 0:
        value = box + magic
        boxes.pop()
        magic_numbers.popleft()
        boxes.append(value)
        continue

    magic_numbers.popleft()
    boxes[-1] += 15

if (("Doll" in presents and "Wooden train" in presents)
        or ("Teddy bear" in presents and "Bicycle" in presents)):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes:
    print(f"Materials left: {', '.join(map(str, reversed(boxes)))}")

if magic_numbers:
    print(f"Magic left: {', '.join(map(str, magic_numbers))}")

for key, value in sorted(presents.items()):
    if value > 0:
        print(f"{key}: {value}")