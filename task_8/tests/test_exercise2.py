from exercise2 import Transform

def test_Transform():
    ascending = "ascending"
    descending = "descending"
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [0, 200]
    l3 = [5, 17, 24, 88, 33, 2]
    l4 = [15, 10, 3]
    l5 = [-90, -100, -888]

    assert Transform(ascending, *l1) == [1, 3, 5, 7, 9, 11]
    assert Transform(descending, *l1) == l1

    assert Transform(ascending, *l2) == [0, 201]
    assert Transform(descending, *l2) == l2

    assert Transform(ascending, *l3) == l3
    assert Transform(descending, *l3) == l3

    assert Transform(ascending, *l4) == l4
    assert Transform(descending, *l4) == [15, 11, 5]

    assert Transform(ascending, *l5) == l5
    assert Transform(descending, *l5) == [-90, -99, -886]