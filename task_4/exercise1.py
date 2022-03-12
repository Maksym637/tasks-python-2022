def transpose(matrix):
    if len(matrix) == 0:
        return 0
    else:
        raws = len(matrix[0])
        column = len(matrix)
        transposed = []
        for i in range (raws):
            transposed.append([])
            for j in range(column):
                transposed[i].append(matrix[j][i])
    return transposed

matrix_1 = [[0, 1, 9],
            [9, 8, 5],
            [7, 3, 1],
            [3, 4, 0]]
matrix_2 = []

if transpose(matrix_1) != 0:
    for t in transpose(matrix_1):
        print(t)
else:
     print("The matrix is empty")