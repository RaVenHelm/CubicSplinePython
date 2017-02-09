import unittest

from cubic_spline import natural_cubic_spline


class MyTestCase(unittest.TestCase):
    def test_natural_spline(self):
        import math
        x = list(range(5))
        n = len(x) - 1
        a = [math.e ** i for i in x]
        splines = natural_cubic_spline(n, x, a)
        print(splines)


if __name__ == '__main__':
    unittest.main()
