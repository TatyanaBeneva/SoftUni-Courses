import re

text = input()
word = input()

pattern = rf"\b{re.escape(word)}\b"
matches = re.findall(pattern, text, re.IGNORECASE)

print(len(matches))