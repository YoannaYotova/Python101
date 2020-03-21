import unittest
from fractions import Fraction, sort_fractions

class TestFraction(unittest.TestCase):
    def test_with_zero_denominator_raise_error(self):
        n = 1
        d = 0
        exc = None
        try:
            res = Fraction(f)
        except Exception as err:
            exc = err

        self.assertIsNotNone(str(exc))
    
    def test_fractions_as_string(self):
        fraction1 = Fraction(1,3)
        fraction2 = Fraction(-1,2)
        fraction3 = Fraction(2,4)

        self.assertEqual(str(fraction1), "1/3")
        self.assertEqual(str(fraction2), "-1/2")
        self.assertEqual(str(fraction3), "2/4")

    def test_equalization_if_fractions_are_equal(self):
        fraction = Fraction(1,3)
        after_simplify = Fraction(1,3)

        self.assertTrue(fraction == after_simplify, 'Fractions are not equal')


    def test_simplified_fraction_is_preserved_after_simplification(self):
        fraction = Fraction(1,3)
        after_simplify = Fraction(1,3)

        self.assertEqual(fraction, after_simplify)

    def test_fraction_is_simplified_after_simplification(self):
        fraction = Fraction(5,25)
        after_simplify = Fraction(1,5)

        self.assertEqual(fraction.simplify(), after_simplify)

    def test_addition_fractions_which_are_simplified_and_with_equal_denominator(self):
        fractoin1 = Fraction(3,7)
        fraction2 = Fraction(1,7)

        res = fractoin1 + fraction2

        self.assertEqual(res, Fraction(4,7))

    def test_addition_fractions_which_are_simplified_and_with_not_equal_denominator(self):
        fractoin1 = Fraction(3,7)
        fraction2 = Fraction(1,3)

        res = fractoin1 + fraction2

        self.assertEqual(res, Fraction(16,21))

    def test_addition_fractions_which_are_not_simplified_and_with_equal_denominator(self):
        fractoin1 = Fraction(2,8)
        fraction2 = Fraction(4,8)

        res = fractoin1 + fraction2

        self.assertEqual(res, Fraction(3,4))

    def test_addition_fractions_which_are_not_simplified_and_with_not_equal_denominator(self):
        fractoin1 = Fraction(2,8)
        fraction2 = Fraction(3,6)

        res = fractoin1 + fraction2

        self.assertEqual(res, Fraction(3,4))

    def test_floating_a_fraction(self):
        fraction = Fraction(1,2)

        res = float(fraction)

        self.assertTrue (res == 0.5)


    def test_sort_fractions_with_multiple_simplified_fractions(self):
        list_of_fractions = [Fraction(2,3), Fraction(1,2), Fraction(1,3)]

        expected_list = [Fraction(1,3), Fraction(1,2), Fraction(2,3)]
        
        res = sort_fractions(list_of_fractions)

        self.assertEqual(res[0], expected_list[0])
        self.assertEqual(res[1], expected_list[1])
        self.assertEqual(res[2], expected_list[2])




if __name__ == '__main__':
    unittest.main()
