SEA_EXCURSION_PRICE = 680
MOUNTAIN_EXCURSION_PRICE = 499

sea_excursion_count = int(input())
mountain_excursion_count = int(input())
sold_see_excursions = 0
sold_mountain_excursions = 0

while True:
    if sea_excursion_count == 0 and mountain_excursion_count == 0:
        print(" Good job! Everything is sold.")
        break

    package_name = input()

    if package_name == "Stop":
        break
    elif package_name == "sea":
        if sea_excursion_count > 0:
            sold_see_excursions += 1
            sea_excursion_count -= 1
    elif package_name == "mountain":
        if mountain_excursion_count > 0:
            sold_mountain_excursions += 1
            mountain_excursion_count -= 1



total_profit = (sold_see_excursions * SEA_EXCURSION_PRICE) + (sold_mountain_excursions * MOUNTAIN_EXCURSION_PRICE)
print(f"Profit: {total_profit} leva.")