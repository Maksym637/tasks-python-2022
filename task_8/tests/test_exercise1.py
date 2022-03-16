from exercise1 import IsSorted

def test_IsSorted_Up():
    order = "ascending"
    assert IsSorted(order, *[1, 2, 3]) == True
    assert IsSorted(order, *[-1, 20, 100, 120, 123, 123]) == True
    assert IsSorted(order, *[0, 0, 0, 12, 34]) == True

    assert IsSorted(order, *[3, 2, 1]) == False
    assert IsSorted(order, *[89, -3, 0, 200]) == False
    assert IsSorted(order, *[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]) == False

def test_IsSorted_Down():
    order = "descending"
    assert IsSorted(order, *[3, 2, 1, 0, -1, -2]) == True
    assert IsSorted(order, *[100, -100]) == True
    assert IsSorted(order, *[0, -3, -4, -5, -88]) == True

    assert IsSorted(order, *[1, 2, 3]) == False
    assert IsSorted(order, *[-1, 20, 100, 120, 123, 123]) == False
    assert IsSorted(order, *[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3]) == False

def test_IsSorted_Error():
    order1 = "something1"
    order2 = "something2"
    order3 = "something3"
    assert IsSorted(order1, *[1, 2, 3]) == False
    assert IsSorted(order2, *[1, 2, 3]) == False
    assert IsSorted(order3, *[1, 2, 3]) == False