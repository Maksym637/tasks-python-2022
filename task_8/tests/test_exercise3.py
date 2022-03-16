from exercise3 import MultArithmeticElements

def test_MultArithmeticElements():
    assert MultArithmeticElements(5, 3, 4) == 6160
    assert MultArithmeticElements(3, 8, 6) == 25478145
    assert MultArithmeticElements(1, 0, 1000) == 1
    assert MultArithmeticElements(1, 1, 6) == 720
    assert MultArithmeticElements(0, 0, 0) == 0
    assert MultArithmeticElements(5, 3, 4) == 6160
    assert MultArithmeticElements(3, -4, 4) == -135