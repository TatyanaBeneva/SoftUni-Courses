last_sector = input()
sector_rows = int(input())
seats_odd_row_count = int(input())
seats_even_row_count = seats_odd_row_count + 2
all_seats = 0

for sector in range(ord("A"), ord(last_sector) + 1):
    for row in range(1, sector_rows + 1):
        seats = seats_odd_row_count

        if row % 2 == 0:
            seats = seats_even_row_count

        for seat in range(1, seats + 1):
            all_seats += 1
            print(f"{chr(sector)}{row}{chr(seat + 96)}")

    sector_rows += 1

print(all_seats)
