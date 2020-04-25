import unittest
from big_possitive_pow import big_possitive_pow
from unittest.mock import patch


class TestBigPossitivePow(unittest.TestCase):
    @patch('big_possitive_pow.randint', side_effect=[12, -1])
    def test_big_possitive_pow_with_y_less_than_one_raise_value_error(self, randint_mock):
        exc = None

        try:
            big_possitive_pow()
        except Exception as err:
            exc = err

        self.assertIsNotNone(str(exc))
        self.assertEqual(str(exc), 'Try again.')

    @patch('big_possitive_pow.randint', side_effect=[2, 3])
    def test_big_possitive_pow_with_correct_x_and_y_returns_x_pow_y(self, randint_mock):

        res = big_possitive_pow()

        self.assertEqual(res, 8)


if __name__ == '__main__':
    unittest.main()
