from calendar import c
from exercise4 import count_ones

def test_count_ones():
    assert count_ones(22) == 3
    assert count_ones(255) == 8
    assert count_ones(64) == 1