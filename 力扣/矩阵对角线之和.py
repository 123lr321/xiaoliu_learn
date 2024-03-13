def diagonalSum(mat):
    mat_length = len(mat)
    if mat_length % 2 != 0:
        sum = 0
        for i in range(0, mat_length):
            sum += mat[i][i] + mat[i][-1 - i]
        return sum
    else:
        sum = 0
        for i in range(0, mat_length):
            if 2*i+1 != mat_length:
                sum += mat[i][i] + mat[i][-1 - i]
            else:
                sum += mat[i][i]
        return sum
