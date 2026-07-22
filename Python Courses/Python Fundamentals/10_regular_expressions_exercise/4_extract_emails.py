import re

text = input()

pattern = r"(?<![A-Za-z0-9._-])[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*@(?:[A-Za-z]+(?:-[A-Za-z]+)*\.)+[A-Za-z]+\b"

emails = re.findall(pattern, text)

print("\n".join(emails))