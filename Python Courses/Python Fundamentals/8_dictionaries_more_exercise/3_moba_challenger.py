def main():
    players = read_players()
    print_players(players)


def read_players() -> dict:
    players = {}

    while True:
        command = input()

        if command == "Season end":
            break

        if " -> " in command:
            player, position, skill = command.split(" -> ")
            skill = int(skill)

            if player not in players:
                players[player] = {}

            if position not in players[player]:
                players[player][position] = skill
            elif players[player][position] < skill:
                players[player][position] = skill

        elif " vs " in command:
            player1, player2 = command.split(" vs ")

            if player1 not in players or player2 not in players:
                continue

            player1_positions = players[player1]
            player2_positions = players[player2]

            has_common_position = False

            for position in player1_positions:
                if position in player2_positions:
                    has_common_position = True
                    break

            if has_common_position:
                player1_total_skill = sum(player1_positions.values())
                player2_total_skill = sum(player2_positions.values())

                if player1_total_skill > player2_total_skill:
                    del players[player2]
                elif player2_total_skill > player1_total_skill:
                    del players[player1]

    return players


def print_players(players: dict):
    sorted_players = sorted(
        players.items(),
        key=lambda item: (-sum(item[1].values()), item[0])
    )

    for player, positions in sorted_players:
        total_skill = sum(positions.values())
        print(f"{player}: {total_skill} skill")

        sorted_positions = sorted(
            positions.items(),
            key=lambda item: (-item[1], item[0])
        )

        for position, skill in sorted_positions:
            print(f"- {position} <::> {skill}")


main()