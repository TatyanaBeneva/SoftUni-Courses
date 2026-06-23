chicken_menu = int(input())
fish_menu = int(input())
vegi_menu = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.4
vegi_menu_price = 8.15

menu_sum = (chicken_menu * chicken_menu_price) + (fish_menu * fish_menu_price) + (vegi_menu * vegi_menu_price)
dessert_price = menu_sum * 0.2

total_sum = menu_sum + dessert_price + 2.5

print(total_sum)