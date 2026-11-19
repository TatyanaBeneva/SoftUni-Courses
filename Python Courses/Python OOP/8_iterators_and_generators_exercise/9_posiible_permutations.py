from itertools import permutations


def possible_permutations(list_num):
    for permutation in permutations(list_num):
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]