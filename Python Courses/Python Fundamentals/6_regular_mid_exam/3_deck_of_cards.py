def add_card(card: str, card_list: list) -> list:
    if card in card_list:
        print("Card is already in the deck")
    else:
        card_list.append(card)
        print("Card successfully added")

    return card_list

def remove_card(card: str, card_list: list) -> list:
    if card in card_list:
        card_list.remove(card)
        print("Card successfully removed")
    else:
        print("Card not found")

    return card_list

def remove_card_at(index: int, card_list: list) -> list:
    if 0 <= index < len(card_list):
        card_list.pop(index)
        print("Card successfully removed")
    else:
        print("Index out of range")

    return card_list

def insert_card(index: int, card: str, card_list: list) -> list:
    if 0 <= index < len(card_list):
        if card in card_list:
            print("Card is already added")
        else:
            card_list.insert(index, card)
            print("Card successfully added")
    else:
        print("Index out of range")

    return card_list

cards = input().split(", ")
lines = int(input())

for _ in range(lines):
    command_list = input().split(", ")
    action = command_list[0]

    if action == "Add":
        cards = add_card(command_list[1], cards)
    if action == "Remove":
        cards = remove_card(command_list[1], cards)
    if action == "Remove At":
        cards = remove_card_at(int(command_list[1]), cards)
    if action == "Insert":
        cards = insert_card(int(command_list[1]), command_list[2], cards)

print(", ".join(cards))