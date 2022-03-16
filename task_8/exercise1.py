def IsSorted(order: str, *arr: list) -> bool:
    unsorted = list(arr)
    sorted_up = unsorted.copy()
    sorted_up.sort()
    sorted_down = unsorted.copy()
    sorted_down.sort(reverse=True)
    if order == "ascending":
        return sorted_up == unsorted
    elif order == "descending":
        return sorted_down == unsorted
    else:
        return False