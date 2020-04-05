import unittest
from collect_fractions import collect_fractions, sum_of_two_fractions


class TestSumOfFractions(unittest.TestCase):
    def test_with_two_fractions_and_zero_denominator(self):
        frac1 = (1, 4)
        frac2 = (2, 0)
        exc = None
        try:
            res = sum_of_two_fractions(frac1, frac2)
        except Exception as err:
            exc = err
        else:
            self.assertEqual(res)

        self.assertIsNotNone(str(exc))
        self.assertEqual(str(exc), 'Cannot divide by zero')

    def test_with_two_fractions(self):
        frac1 = (1, 4)
        frac2 = (2, 8)

        res = sum_of_two_fractions(frac1, frac2)

        self.assertEqual(res, (1, 2))


class TestCollectFractions(unittest.TestCase):
    def test_with_onee_fractions(self):
        fractions = [(1, 2)]

        res = collect_fractions(fractions)

        self.assertEqual(res, (1, 2))

    def test_with_many_fractions(self):
        fractions = [(2, 8), (4, 6), (1, 2)]

        res = collect_fractions(fractions)

        self.assertEqual(res, (17, 12))


if __name__ == '__main__':
    unittest.main()
