def setZeroes(matrix):
    import copy
    matrix_text = copy.deepcopy(matrix)
    length=len(matrix)
    width=len(matrix[0])
    for i in range(0, length):
        for j in range(0, width):
            if matrix[i][j] == 0:
                for r in range(0,width):
                    matrix_text[i][r] = 0
                for k in range(0, len(matrix)):
                    matrix_text[k][j] = 0
    matrix = matrix_text
    return matrix
print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))