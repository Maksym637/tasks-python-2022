from exercise3 import get_shortest_word

def test_get_shortest_word():
    assert get_shortest_word("") == "The string is empty"
    assert get_shortest_word("   ") == "The string is empty"
    assert get_shortest_word("  \n \n \t \t  ") == "The string is empty"
    assert get_shortest_word("Python is simple") == "is"
    assert get_shortest_word("What do you think about it?") == "do"
    assert get_shortest_word("    Stop   before   you   finish   that   sentence   ") == "you"
    assert get_shortest_word("\n I loved\t    her") == "I"
    assert get_shortest_word("\nMoney\n is the anthem of success\n") == "is"