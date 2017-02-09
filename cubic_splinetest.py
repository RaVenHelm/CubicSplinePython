import unittest

from cubic_spline import natural_cubic_spline, clamped_cubic_spline


class MyTestCase(unittest.TestCase):
    def test_natural_spline(self):
        import math
        x = list(range(5))
        n = len(x) - 1
        a = [math.e ** i for i in x]
        splines = natural_cubic_spline(n, x, a)
        # print(splines)

    def test_clamped_spline(self):
        x = [1, 2, 3]
        n = len(x) - 1
        a = [2, 3, 5]
        primes = (2, 1)
        sols = [(2.0, 2.0, -2.5, 1.5), (3.0, 1.5, 2.0, -1.5)]
        for idx, spline in enumerate(clamped_cubic_spline(n, x, a, primes)):
            solution = sols[idx]
            self.assertTupleEqual(solution, spline)

    def test_spline_two(self):
        from math import e
        x = list(range(4))
        n = len(x) - 1
        a = [e ** i for i in x]
        primes = (1, e ** 3)
        solutions = [
            (1.0, 1.0, 0.44468, 0.27360),
            (2.71828, 2.71016, 1.26548, 0.69513),
            (7.38906, 7.32652, 3.35087, 2.01909)
        ]
        for idx, spline in enumerate(clamped_cubic_spline(n, x, a, primes)):
            solution = solutions[idx]
            self.assertTupleEqual(solution, spline)

if __name__ == '__main__':
    unittest.main()
