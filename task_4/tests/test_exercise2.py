from exercise2 import factorial_1, factorial_2

def test_factorial_1():
    assert factorial_1(0) == 1
    assert factorial_1(1) == 1
    assert factorial_1(6) == 720
    assert factorial_1(8) == 40320

def test_factorial_2():
    assert factorial_2(0) == 1
    assert factorial_2(1) == 1
    assert factorial_2(3) == 6
    assert factorial_2(8) == 40320