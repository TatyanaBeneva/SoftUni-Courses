words = input().split()
words_dict = {}

for word in words:
    word_lower = word.lower()

    if word_lower not in words_dict:
        words_dict[word_lower] = 0

    words_dict[word_lower] += 1

for word, count in words_dict.items():
    if count % 2 != 0:
        print(word, end=" ")