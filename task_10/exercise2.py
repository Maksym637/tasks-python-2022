def isPalindromeString(string: str) -> bool:
    return string == string[::-1]

def isPalindromeInteger(x: int) -> bool:
    if x < 0:
        return False
    
    rev_num = 0
    digit = 0

    while x // pow(10, digit) != 0:
        rev_num = (rev_num * 10) + (x // pow(10, digit) % 10)
        digit += 1
    
    return x == rev_num