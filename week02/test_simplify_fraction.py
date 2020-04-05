import unittest
from simplify_fraction import simplify_fraction, gcd


class TestGreatestCommonDevisor(unittest.TestCase):
    def test_devision_by_zero(self):
        exc = None
        try:
            gcd(3, 0)
        except Exception as err:
            exc = err

        self.assertIsNotNone(str(exc))
        self.assertEqual(str(exc), 'Cannot divide by zero')

    def test_with_reducible_fraction(self):
        res = gcd(12, 8)

        self.assertEqual(res, 4)

    def test_with_irreducible_fraction(self):
        res = gcd(9, 28)

        self.assertEqual(res, 1)


class TestSimplifyFraction(unittest.TestCase):
    def test_with_reducible_fraction(self):
        fraction = (462, 63)

        res = simplify_fraction(fraction)

        self.assertEqual(res, (22, 3))

    def test_with_irreducible_fraction(self):
        fraction = (1, 7)

        res = simplify_fraction(fraction)

        self.assertEqual(res, (1, 7))


if __name__ == '__main__':
    unittest.main()
