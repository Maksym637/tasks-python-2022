from exercise5 import count_letters

def test_count_letters():
    assert count_letters("stringsample") == {'s': 2, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1, 'e': 1}
    assert count_letters("") == {}
    assert count_letters("HelloPython") == {'H': 1, 'e': 1, 'l': 2, 'o': 2, 'P': 1, 'y': 1, 't': 1, 'h': 1, 'n': 1}
    assert count_letters("ooooooooooppppp###") == {'o': 10, 'p': 5, '#': 3}
    assert count_letters("__init__( )") == {'_': 4, 'i': 2, 'n': 1, 't': 1, '(': 1, ' ': 1, ')': 1,}