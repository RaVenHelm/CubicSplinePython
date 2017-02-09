def main():
    import numpy as np
    import matplotlib.pyplot as plt

    from cubic_spline import clamped_cubic_spline, spline_function

    csv = np.genfromtxt('snoopy_one.csv', delimiter=',', skip_header=1)
    x_values_one = csv[:, 0]
    fx_values_one = csv[:, 1]
    primes = csv[:, 2]
    primes_one = primes[0], primes[-1]
    splines = clamped_cubic_spline(len(x_values_one) - 1, x_values_one, fx_values_one, primes_one)

    graph_x = []
    graph = []
    subinterval = 50

    for idx, spline in enumerate(splines):
        x0, x1 = x_values_one[idx], x_values_one[idx + 1]
        diff = round((x1 - x0) / subinterval, 10)
        graph_x.append(x0)
        graph.append(fx_values_one[idx])
        for i in range(subinterval):
            graph_x.append(round(x0 + diff, 10))
            result = spline_function(*spline, x0, x0 + diff)
            graph.append(round(result, 10))

    graph_x.append(x_values_one[-1])
    graph.append(fx_values_one[-1])

    csv = np.genfromtxt('snoopy_two.csv', delimiter=',', skip_header=1)
    x_values_two = csv[:, 0]
    fx_values_two = csv[:, 1]
    primes = csv[:, 2]
    primes_two = primes[0], primes[-1]
    splines = clamped_cubic_spline(len(x_values_two) - 1, x_values_two, fx_values_two, primes_two)

    for idx, spline in enumerate(splines):
        x0, x1 = x_values_two[idx], x_values_two[idx + 1]
        diff = round((x1 - x0) / subinterval, 5)
        graph_x.append(x0)
        graph.append(fx_values_two[idx])
        for i in range(subinterval):
            graph_x.append(round(x0 + diff, 5))
            result = spline_function(*spline, x0, x0 + diff)
            graph.append(round(result, 5))

    graph_x.append(x_values_two[-1])
    graph.append(fx_values_two[-1])

    csv = np.genfromtxt('snoopy_three.csv', delimiter=',', skip_header=1)
    x_values_three = csv[:, 0]
    fx_values_three = csv[:, 1]
    primes = csv[:, 2]
    primes_three = primes[0], primes[-1]
    splines = clamped_cubic_spline(len(x_values_three) - 1, x_values_three, fx_values_three, primes_three)

    for idx, spline in enumerate(splines):
        x0, x1 = x_values_three[idx], x_values_three[idx + 1]
        diff = round((x1 - x0) / subinterval, 5)
        graph_x.append(x0)
        graph.append(fx_values_three[idx])
        for i in range(subinterval):
            graph_x.append(round(x0 + diff, 5))
            result = spline_function(*spline, x0, x0 + diff)
            graph.append(round(result, 5))

    graph_x.append(x_values_three[-1])
    graph.append(fx_values_three[-1])

    plt.plot(x_values_one,
             fx_values_one,
             'bo',
             x_values_two,
             fx_values_two,
             'bo',
             x_values_three,
             fx_values_three,
             'bo',
             graph_x,
             graph,
             'r-')
    plt.axis([0, 30, 0, 8])
    plt.show()


if __name__ == '__main__':
    main()
