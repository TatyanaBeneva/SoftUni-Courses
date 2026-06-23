VIDEO_CARD_PRICE = 250

budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_memory_count = int(input())

video_cards_sum = VIDEO_CARD_PRICE * video_cards_count
processors_sum = processors_count * (video_cards_sum * 0.35)
ram_memory_sum = ram_memory_count * (video_cards_sum * 0.10)

total_sum = video_cards_sum + processors_sum + ram_memory_sum

if video_cards_count > processors_count:
    total_sum = total_sum - (total_sum * 0.15)

if total_sum > budget:
    print(f"Not enough money! You need {(total_sum - budget):.2f} leva more!")
else:
    print(f"You have {(budget - total_sum):.2f} leva left!")