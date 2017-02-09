import unittest

from crout_factorization import augment_matrix, crout_factorization


class CroutFactorization(unittest.TestCase):
    def test_crout(self):
        mat = [[2, -1, 0, 0],
               [-1, 2, -1, 0],
               [0, -1, 2, -1],
               [0, 0, -1, 2]]

        solution = [1, 0, 0, 1]

        augment_matrix(mat, solution)

        approx = crout_factorization(len(solution), mat)
        ans = [1.0] * 4
        for pair in zip(approx, ans):
            self.assertAlmostEqual(pair[0], pair[1])


if __name__ == '__main__':
    unittest.main()
