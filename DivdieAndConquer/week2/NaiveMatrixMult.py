# Input: nxn integer matrices
# Output: Z = x * y
def naive_matrix_mult(x, y):
    z = []
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            z[i][j] = 0
            for k in range(0, len(y)):
                z[i][j] += x[i][k] * y[k][j]
    return z