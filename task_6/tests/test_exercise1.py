from exercise1 import average

def test_average():
    assert average(1, 2) == "{0:.2f}".format(1.5)
    assert average(2, 3, 4, 100, 12, 7, 8, 0) == "{0:.2f}".format(17)
    assert average(2, 2, 2, 2, 2, 2) == "{0:.2f}".format(2)
    assert average(100, 250, 15, 17, 80, -91, 155) == "{0:.2f}".format(75.1428)
