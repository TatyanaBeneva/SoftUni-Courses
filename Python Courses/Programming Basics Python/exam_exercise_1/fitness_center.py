clients_count = int(input())

back_activity_counter = 0
chest_activity_counter = 0
legs_activity_counter = 0
abs_activity_counter = 0
protein_shake_counter = 0
protein_bar_counter = 0

for client in range(clients_count):
    fitness_activity = input()

    if fitness_activity == "Back":
        back_activity_counter += 1
    elif fitness_activity == "Chest":
        chest_activity_counter += 1
    elif fitness_activity == "Legs":
        legs_activity_counter += 1
    elif fitness_activity == "Abs":
        abs_activity_counter += 1
    elif fitness_activity == "Protein shake":
        protein_shake_counter += 1
    elif fitness_activity == "Protein bar":
        protein_bar_counter += 1

training_people_count = back_activity_counter + chest_activity_counter + legs_activity_counter + abs_activity_counter
protein_byers = protein_shake_counter + protein_bar_counter

print(f"{back_activity_counter} - back")
print(f"{chest_activity_counter} - chest")
print(f"{legs_activity_counter} - legs")
print(f"{abs_activity_counter} - abs")
print(f"{protein_shake_counter} - protein shake")
print(f"{protein_bar_counter} - protein bar")
print(f"{training_people_count / clients_count * 100:.2f}% - work out")
print(f"{protein_byers / clients_count * 100:.2f}% - protein")
