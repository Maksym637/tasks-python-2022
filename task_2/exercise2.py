
def swapping(arr):
    first_element = arr[0]
    last_element = arr[len(arr) - 1]
    arr_new = arr.copy()
    arr_new[0] = last_element
    arr_new[len(arr_new) - 1] = first_element
    return arr_new


players = ['player1', 'player2', 'player3', 'player4', 'player5']
print(swapping(swapping(players)))