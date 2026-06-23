USD_TO_BGN = 1.57

processor_price_usd = float(input())
video_card_price_usd = float(input())
ram_price_usd = float(input())
ram_count = int(input())
discount_percent = float(input())

processor_price = processor_price_usd * USD_TO_BGN
video_card_price = video_card_price_usd * USD_TO_BGN
ram_price = ram_price_usd * USD_TO_BGN
ram_sum = ram_count * ram_price
discount = (processor_price + video_card_price) * discount_percent

total_sum = (processor_price + video_card_price + ram_sum) - discount
print(f"Money needed - {total_sum:.2f} leva.")