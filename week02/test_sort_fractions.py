import unittest
from sort_fractions import sort_fractions, checking_for_zero_denominator

class TestCheckingForZeroDenominator(unittest.TestCase):
    def test_for_zero_denominator(self):
        fractions = [(3,0) , (1,2)]
        exc = None

        try:
            checking_for_zero_denominator(fractions)
        except Exception as err:
            exc = err

        self.assertIsNotNone(str(exc))
        self.assertEqual(str(exc), 'Cannot devide by zero')


class TestSortFractions(unittest.TestCase):
    def test_with_empty_list(self):
        fractions = []

        res = sort_fractions(fractions)

        self.assertEqual(res,fractions)

    def test_with_one_fraction(self):
        fractions = [(1,2)]

        res = sort_fractions(fractions)

        self.assertEqual(res, fractions)

    def test_with_more_fractions_and_default_ascending_true(self):
        fractions = [(2, 3), (1, 2), (1, 3)]

        res = sort_fractions(fractions)

        self.assertEqual(res, [(1, 3), (1, 2), (2, 3)])

    def test_with_more_fractions_and_false_ascending(self):
        fractions = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]

        res = sort_fractions(fractions, ascending = False)

        self.assertEqual(res,[(22, 7), (9, 6), (7, 8), (5, 6), (15, 32), (22, 78)])


if __name__ == '__main__':
    unittest.main()
