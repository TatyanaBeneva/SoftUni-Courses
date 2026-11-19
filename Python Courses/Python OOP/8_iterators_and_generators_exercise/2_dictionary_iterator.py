class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.dictionary):
            raise StopIteration

        items = list(self.dictionary.items())
        key, value = items[self.current]
        self.current += 1
        return (key, value)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

