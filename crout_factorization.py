""" crout_factorization.py
Implementation of the Crout Factorization method
link: https://en.wikipedia.org/wiki/Crout_matrix_decomposition
"""


def crout_factorization(n, matrix):
    sols = [0.0] * n

    l = [[0.0] * n for _ in range(n)]
    u = [[0.0] * n for _ in range(n)]
    for i in range(n):
        u[i][i] = 1.0
    z = [0.0] * n

    # step 1
    l[0][0] = matrix[0][0]
    if l[0][0] == 0.0:
        raise TypeError('a(1,1) must not be zero!')
    u[0][1] = matrix[0][1] / l[0][0]
    z[0] = matrix[0][n] / l[0][0]

    # step 2
    for i in range(1, n-1):
        l[i][i-1] = matrix[i][i-1]
        l[i][i] = matrix[i][i] - l[i][i-1] * u[i-1][i]
        u[i][i+1] = matrix[i][i+1] / l[i][i]
        var = (matrix[i][n] - l[i][i - 1] * z[i - 1]) / l[i][i]
        z[i] = var

    # step 3
    l[-1][-2] = matrix[n-1][n-2]
    l[-1][-1] = matrix[n-1][n-1] - l[-1][-2] * u[-2][-1]
    z[-1] = (matrix[-1][n] - l[-1][-2] * z[-2]) / l[-1][-1]

    # step 4
    sols[-1] = z[-1]
    for i in range(n-1, 0, -1):
        sols[i-1] = z[i-1] - u[i-1][i] * sols[i]

    return sols


def augment_matrix(mat, vec):
    for idx, row in enumerate(mat):
        row.append(vec[idx])


def main():
    return


if __name__ == '__main__':
    main()
