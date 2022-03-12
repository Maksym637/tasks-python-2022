from exercise1 import transpose

def test_transpose():
    assert transpose([[1, 2, 3, 4],[5, 6, 7, 8]]) == [[1, 5], [2, 6], [3, 7], [4, 8]]

    assert transpose([[1, 2],[3, 4]]) == [[1, 3], [2, 4]]

    assert transpose([[0, 1, 9], [9, 8, 5], [7, 3, 1], [3, 4, 0]]) == [[0, 9, 7, 3], [1, 8, 3, 4], [9, 5, 1, 0]]

    assert transpose([]) == 0