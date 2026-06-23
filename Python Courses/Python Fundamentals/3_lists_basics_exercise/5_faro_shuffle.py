array_of_cards = input().split()
faro_shuffles_count = int(input())

half_length = len(array_of_cards) // 2

for _ in range(faro_shuffles_count):
    shuffled_cards_deck = array_of_cards.copy()

    for index in range(half_length):
        shuffled_cards_deck[2 * index] = array_of_cards[index]
        shuffled_cards_deck[2 * index + 1] = array_of_cards[index + half_length]

    array_of_cards = shuffled_cards_deck

print(array_of_cards)