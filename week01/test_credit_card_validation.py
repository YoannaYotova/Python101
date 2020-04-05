import unittest
from credit_card_validation import sum_of_digits, is_credit_card_valid


class TestSumOfDigits(unittest.TestCase):
    def test_with_single_digit(self):
        n = 3

        res = sum_of_digits(n)

        self.assertEqual(res, n)

    def test_with_more_digits(self):
        n = 301

        res = sum_of_digits(n)

        self.assertEqual(res, 4)


class TestIsCreditCardValid(unittest.TestCase):
    def test_with_even_digits_of_card_raise_error(self):
        credit_card = 123456
        exc = None

        try:
            is_credit_card_valid(credit_card)
        except Exception as err:
            exc = err

        self.assertIsNotNone(str(exc))
        self.assertEqual(str(exc), 'Invalid credit card')

    def test_with_correct_card_but_invalid_return_false(self):
        credit_card = 1234567

        res = is_credit_card_valid(credit_card)

        self.assertEqual(res, False)

    def test_with_correct_and_valid_card_return_true(self):
        credit_card = 79927398713

        res = is_credit_card_valid(credit_card)

        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
