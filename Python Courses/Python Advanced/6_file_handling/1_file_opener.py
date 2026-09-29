try:
    with open("text.txt", "r") as file:
        print("file found")
        print(file.read())
except FileNotFoundError:
    print("file not found")