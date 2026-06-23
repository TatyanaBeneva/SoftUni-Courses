level_of_fire = input().split("#")
amount_of_water = int(input())
cells_put_out_the_fire = []
effort = 0.0

for index in range(len(level_of_fire)):
    current_level_array = level_of_fire[index].split(" = ")
    fire = current_level_array[0]
    cell = int(current_level_array[1])

    if (fire == "High" and (cell < 81 or cell > 125)) or \
            (fire == "Medium" and (cell < 51 or cell > 80)) or \
            (fire == "Low" and (cell < 1 or cell > 50)):
        continue

    if amount_of_water - cell >= 0:
        amount_of_water -= cell
        effort += cell * 0.25
        cells_put_out_the_fire.append(cell)

total_fire = sum(cells_put_out_the_fire)

print("Cells:")

for cell in cells_put_out_the_fire:
    print(f" - {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
