import string

def test_1_1(*lis: list) -> set:
    if len(lis) == 0:
        return 0
    return set.intersection(*map(set, lis))

def test_1_2(*lis: list) -> set:
    if len(lis) == 0:
        return 0
    union = set.union(*map(set, lis))
    listSet = list(map(set, lis))
    for i in range(len(listSet)):
        for j in range(1, len(listSet) - i):
            union.difference_update(set(listSet[i]).intersection(set(listSet[j + i])))
    return union

def test_1_3(*lis: list) -> set:
    if len(lis) == 0:
        return 0
    union = set.union(*map(set, lis))
    nonrep = test_1_2(*lis)
    return union.difference(nonrep)

def test_1_4(*lis: list) -> set:
    if len(lis) == 0:
        return 0
    alphabet = set(string.ascii_lowercase)
    union = set.union(*map(set, lis))
    return alphabet.difference(union)