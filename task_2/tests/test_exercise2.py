from exercise2 import swapping

def test_swapping_1():
    arr = ['player1', 'player2', 'player3', 'player4', 'player5']
    arr_swapped = ['player5', 'player2', 'player3', 'player4', 'player1']
    assert swapping(arr) == arr_swapped

def test_swapping_2():
    arr = ['a', 'b', 'c', 'd', 'e']
    arr_swapped = ['e', 'b', 'c', 'd', 'a']
    assert swapping(arr) == arr_swapped

def test_swapping_3():
    arr = [1, 2, 3, 4, 5]
    arr_swapped = [5, 2, 3, 4, 1]
    assert swapping(arr) == arr_swapped