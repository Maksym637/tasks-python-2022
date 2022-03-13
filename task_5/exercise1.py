def spiral(n: int, m: int) -> list:
    # initial values
    top = left = 0
    bottom = n - 1
    right = m - 1
    count = 1

    # filling the matrix with zeros
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(0)
 
    while True:
        if left > right:
            break
 
        # top row
        for i in range(left, right + 1):
            matrix[top][i] = count
            count = count + 1
        top = top + 1
 
        if top > bottom:
            break
 
        # right column
        for i in range(top, bottom + 1):
            matrix[i][right] = count
            count = count + 1
        right = right - 1
 
        if left > right:
            break
 
        # bottom row
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = count
            count = count + 1
        bottom = bottom - 1
 
        if top > bottom:
            break
 
        # left column
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = count
            count = count + 1
        left = left + 1

    return matrix

for res in spiral(3, 3):
    print(res)