cards_string = input()
array_of_cards = cards_string.split(" ")
unic_array_of_cards = []

for card in array_of_cards:
    if card not in unic_array_of_cards:
        unic_array_of_cards.append(card)

team_a_players = 11
team_b_players = 11
is_game_terminated = False

for card in unic_array_of_cards:
    card_array = card.split("-")

    if card_array[0] == "A":
        team_a_players -= 1
    elif card_array[0] == "B":
        team_b_players -= 1

    if team_a_players < 7 or team_b_players < 7:
        is_game_terminated = True
        break

print(f"Team A - {team_a_players}; Team B - {team_b_players}")

if is_game_terminated:
    print("Game was terminated")