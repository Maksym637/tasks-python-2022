from exercise3 import fib_sum

def test_fib_sum():
    assert fib_sum(-3) == 0
    assert fib_sum(0) == 0

    assert fib_sum(4) == 7
    assert fib_sum(5) == 12
    assert fib_sum(10) == 143
    assert fib_sum(12) == 376