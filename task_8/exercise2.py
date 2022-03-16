from exercise1 import IsSorted

def Transform(order: str, *arr: list) -> list:
    array = list(arr)
    result = array.copy()
    if IsSorted(order, *arr):
        for i in range(len(array)):
            result[i] = array[i] + i
        return result
    else:
        return array