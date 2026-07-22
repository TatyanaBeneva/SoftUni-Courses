import re

pattern = r"www\.[A-Za-z0-9-]+(?:\.[a-z]+)+"

while True:
    try:
        text = input()
    except EOFError:
        break

    links = re.findall(pattern, text)

    for link in links:
        print(link)