data = input()
phonebook = {}

while not data.isdigit():
    name, number = data.split("-")
    phonebook[name] = number
    data = input()

for _ in range(int(data)):
    people_name = input()

    if people_name in phonebook:
        print(f"{people_name} -> {phonebook[people_name]}")
    else:
        print(f"Contact {people_name} does not exist.")