text = input()

sorted_text = [ch for ch in text if ch.lower() not in ['a', 'u', 'o', 'e', 'i']]

print("".join(sorted_text))