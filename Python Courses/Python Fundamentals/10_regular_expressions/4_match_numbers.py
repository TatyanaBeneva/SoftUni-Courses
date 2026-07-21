import re

text = input()

regex = r"(^|(?<=\s))-?(?:0|[1-9]\d*)(?:\.\d+)?($|(?=\s))"

matches = re.finditer(regex, text)

print(" ".join(match.group() for match in matches))