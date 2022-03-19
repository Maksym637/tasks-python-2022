from exercise2 import most_common_words

path1 = 'data/text1.txt'
path2 = 'data/text2.txt'
path3 = 'data/text3.txt'

def test_1():
    assert most_common_words(path1, 15) == ['the']
    assert most_common_words(path1, 3) == ['And', 'are', 'is', 'of', 'with']
    assert most_common_words(path1, 4) == ['so', 'to']

def test_2():
    assert most_common_words(path2, 2) == ['full', 'of']
    assert most_common_words(path2, 1) == ['eat', 'juicy', 'messy', 'sweet', 'to', 'treat', 'water']

def test_3():
    assert most_common_words(path3, 5) == ['a']
    assert most_common_words(path3, 2) == ['arr', 'b', 'smth']
    assert most_common_words(path3, 1) == ['c', 'd']