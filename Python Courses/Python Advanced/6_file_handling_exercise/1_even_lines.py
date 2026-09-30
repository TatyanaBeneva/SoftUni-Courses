symbols = ("-", ",", ".", "!", "?")

with open("text.txt", encoding="utf-8") as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            for symbol in symbols:
                line = line.replace(symbol, "@")

            print(" ".join(reversed(line.split())))