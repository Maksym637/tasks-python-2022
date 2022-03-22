from exercise1 import Circle, Ring

circle1 = Circle(10)
circle2 = Circle(8)
ring1 = Ring(3)
ring2 = Ring(4)

def test_get():
    assert circle1.radius == 10
    assert circle2.radius == 8
    assert ring1.ring == 3
    assert ring2.ring == 4

def test_str():
    assert circle1.__str__() == "The circle radius is 10"
    assert circle2.__str__() == "The circle radius is 8"
    assert ring1.__str__() == "The ring radius is 3"
    assert ring2.__str__() == "The ring radius is 4"

def test_area():
    assert circle1.area() == 314.1592653589793
    assert circle2.area() == 201.06192982974676
    assert ring1.area(circle1) == 285.88493147667117
    assert ring2.area(circle2) == 150.79644737231007

def test_increase():
    assert circle1.increase(50) == 500
    assert circle2.increase(10) == 80
    assert ring1.increase(4) == 12
    assert ring2.increase(50) == 200

def test_big():
    Circle.isBig(10) == False
    Circle.isBig(200) == True
    Ring.isBig(22) == False
    Ring.isBig(101) == True

def test_add():
    assert (circle1 + circle2).radius == 18
    assert (Circle(22) + Circle(13)).radius == 35

def test_sub():
    assert (circle1 - circle2).radius == 2
    assert (Circle(22) - Circle(13)).radius == 9