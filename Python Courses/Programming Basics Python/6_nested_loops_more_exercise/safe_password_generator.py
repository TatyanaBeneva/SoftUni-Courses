a = int(input())
b = int(input())
max_passwords = int(input())

count = 0

symbol_a = 35
symbol_b = 64

for x in range(1, a + 1):
    for y in range(1, b + 1):
        if count >= max_passwords:
            break

        print(f"{chr(symbol_a)}{chr(symbol_b)}{x}{y}{chr(symbol_b)}{chr(symbol_a)}", end="|")

        count += 1

        symbol_a += 1
        symbol_b += 1

        if symbol_a > 55:
            symbol_a = 35

        if symbol_b > 96:
            symbol_b = 64

    if count >= max_passwords:
        break