def solution():
    def integers():
        counter = 1
        while True:
            yield counter
            counter += 1

    def halves():
        for i in integers():
            yield i / 2


    def take(n, seq):
        iterator = iter(seq)
        result = []
        for index in range(n):
            result.append(next(iterator))
        return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
