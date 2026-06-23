words = input()
list_of_words = words.split(", ")
index_of_wolf = list_of_words.index("wolf")
sheep_number = len(list_of_words) - (index_of_wolf - 1)

if index_of_wolf + 1 == len(list_of_words):
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")