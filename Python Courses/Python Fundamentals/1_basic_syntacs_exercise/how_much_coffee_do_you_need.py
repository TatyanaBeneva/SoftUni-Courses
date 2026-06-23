command = input()
number_of_coffees = 0

while command != "END":
    if command == "coding" or\
            command == "cat" or\
            command == "dog" or\
            command == "movie":
        number_of_coffees += 1
    elif command == "CODING" or\
            command == "CAT" or\
            command == "DOG" or\
            command == "MOVIE":
        number_of_coffees += 2

    command = input()

if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)