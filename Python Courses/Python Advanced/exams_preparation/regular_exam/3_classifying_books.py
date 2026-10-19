def classify_books(*args, **kwargs):
    fiction_titles = set()
    non_fiction_titles = set()

    for genre, title in args:
        if genre == "fiction":
            fiction_titles.add(title)
        else:
            non_fiction_titles.add(title)

    fiction_books = {}
    non_fiction_books = {}

    for isbn, title in kwargs.items():
        if title in fiction_titles:
            fiction_books[isbn] = title
        if title in non_fiction_titles:
            non_fiction_books[isbn] = title

    result = []

    if fiction_books:
        result.append("Fiction Books:")
        for isbn, title in sorted(fiction_books.items()):
            result.append(f"~~~{isbn}#{title}")

    if non_fiction_books:
        result.append("Non-Fiction Books:")
        for isbn, title in sorted(non_fiction_books.items(), reverse=True):
            result.append(f"***{isbn}#{title}")

    return "\n".join(result)

print(classify_books(
    ("fiction", "Brave New World"),
    ("non_fiction", "The Art of War"),
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))

print(classify_books(
    ("non_fiction", "The Art of War"),
    ("fiction", "The Great Gatsby"),
    ("non_fiction", "A Brief History of Time"),
    ("fiction", "Brave New World"),
    FF1234HH="The Great Gatsby",
    NF3845UU="A Brief History of Time",
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))

print(classify_books(
    ("fiction", "Brave New World"),
    ("fiction", "The Catcher in the Rye"),
    ("fiction", "1984"),
    FICCITRZZ="The Catcher in the Rye",
    FIC1984XX="1984",
    FICBNWYYY="Brave New World"
))

print(classify_books(
    ("non_fiction", "Sapiens"),
    ("non_fiction", "Homo Deus"),
    ("non_fiction", "The Selfish Gene"),
    NF123ABC="Sapiens",
    NF987XYZ="Homo Deus",
    NF456DEF="The Selfish Gene"
))
