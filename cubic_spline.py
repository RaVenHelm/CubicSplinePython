"""cubic_spline.py
Implementations of the natural (and maybe clamped) cubic spline algorithms
"""


def natural_cubic_spline(n, x, a):
    b = [0.0] * (n + 1)
    c = [0.0] * (n + 1)
    d = [0.0] * (n + 1)
    u = [0.0] * n
    l = [0.0] * (n + 1)
    z = [0.0] * (n + 1)

    # step 1
    h = [x[i + 1] - x[i] for i in range(n)]

    def calculate_matrix_entry(i):
        return (3.0 / h[i]) * (a[i+1] - a[i]) - (3.0/h[i-1]) * (a[i] - a[i-1])

    # step 2
    alpha = [calculate_matrix_entry(i) for i in range(1, n)]
    l[0] = 1
    u[0] = 0
    z[0] = 0

    for i in range(1, n):
        l[i] = 2 * (x[i+1] - x[i-1]) - (h[i-1] * u[i-1])
        u[i] = h[i]/l[i]
        z[i] = (alpha[i-1] - h[i-1] * z[i-1]) / l[i]

    l[n] = 1
    z[n] = 0
    c[n] = 0

    for j in range(n-1, -1, -1):
        c[j] = z[j] - u[j]*c[j+1]
        b[j] = (a[j+1] - a[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3
        d[j] = (c[j+1] - c[j]) / (3*h[j])

    return list(zip(a[:-1], b[:-1], c[:-1], d[:-1]))


if __name__ == '__main__':
    import math
    from pprint import pprint
    x = list(range(5))
    n = len(x) - 1
    a = [math.e ** i for i in x]
    splines = natural_cubic_spline(n, x, a)
    for idx, spline in enumerate(splines):
        print('S({})='.format(idx), end=' ')
        pprint(spline)

    x = 2.001
    ans = math.e ** x
    def eqn_2(x):
        spline = splines[2]
        return spline[0] + spline[1] * (x - 2) + spline[2] * (x - 2) ** 2 + spline[3] * (x - 2) ** 3

    approx = eqn_2(x)
    print('e^{:.3f} = {:.7f}'.format(x, ans))
    print('e^{:.3f} is approx. = {:.7f}'.format(x, approx))
