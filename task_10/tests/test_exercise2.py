from exercise2 import isPalindromeString, isPalindromeInteger

def test_isPalindromeString():
    assert isPalindromeString("redivider") == True
    assert isPalindromeString("level") == True
    assert isPalindromeString("abccba") == True

    assert isPalindromeString("hello") == False
    assert isPalindromeString("cool") == False
    assert isPalindromeString("abcdefg") == False

def test_isPalindromeInteger():
    assert isPalindromeInteger(121) == True
    assert isPalindromeInteger(44) == True
    assert isPalindromeInteger(123321) == True

    assert isPalindromeInteger(-121) == False
    assert isPalindromeInteger(10) == False
    assert isPalindromeInteger(123456) == False