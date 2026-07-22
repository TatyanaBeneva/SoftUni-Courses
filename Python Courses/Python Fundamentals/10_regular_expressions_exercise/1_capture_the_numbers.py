import re

matches = []
line = input()

while line:
    matches.extend(re.findall(r"\d+", line))
    line = input()

print(" ".join(matches))