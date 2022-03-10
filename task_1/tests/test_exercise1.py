from exercise1 import triangle_area

def test_triangle_area_1():
    assert triangle_area(3, 4, 5) == "{0:.2f}".format(6)

def test_triangle_area_2():
    assert triangle_area(4.5, 5.9, 9) == "{0:.2f}".format(11.5831)

def test_triangle_area_3():
    assert triangle_area(3, 3, 3) == "{0:.2f}".format(3.8971)

def test_triangle_area_error():
    assert triangle_area(1, 3, 20) == -1