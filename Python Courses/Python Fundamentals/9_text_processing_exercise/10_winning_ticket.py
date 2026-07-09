def main():
    tickets = input().split(", ")

    for ticket in tickets:
        ticket = ticket.strip()

        if len(ticket) != 20:
            print("invalid ticket")
            continue

        left = ticket[:10]
        right = ticket[10:]

        count, symbol = get_winning_match(left, right)

        if count is None:
            print(f'ticket "{ticket}" - no match')
        elif count == 10:
            print(f'ticket "{ticket}" - {count}{symbol} Jackpot!')
        else:
            print(f'ticket "{ticket}" - {count}{symbol}')


def get_winning_match(left, right):
    symbols = ["@", "#", "$", "^"]

    for symbol in symbols:
        for count in range(10, 5, -1):
            sequence = symbol * count

            if sequence in left and sequence in right:
                return count, symbol

    return None, None

main()