import pytest
from exercise1 import Triangle, Point

triangle = Triangle(Point(0, 0), Point(-1, 1), Point(1, 1))

def test_is_point_inside_true():
    point1 = Point(0.5,0.5)
    assert triangle.is_point_inside(point1) == True

    point2 = Point(0,0)
    assert triangle.is_point_inside(point2) == True

    point3 = Point(-0.5,0.8)
    assert triangle.is_point_inside(point3) == True

def test_is_point_inside_false():
    point1 = Point(0.5,0.4)
    assert triangle.is_point_inside(point1) == False

    point2 = Point(1,-1)
    assert triangle.is_point_inside(point2) == False

    point3 = Point(-0.8,0.5)
    assert triangle.is_point_inside(point3) == False