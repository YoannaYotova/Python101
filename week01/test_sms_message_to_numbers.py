from sms_message_to_numbers import message_into_numbers
import unittest


class TestConvertMessagiIntoNumbers(unittest.TestCase):
    def test_with_empty_string_raise_error(self):
        message = ""
        exc = None

        try:
            message_into_numbers(message)
        except Exception as err:
            exc = err

        self.assertIsNotNone(str(exc))
        self.assertEqual(str(exc), 'Empty message')

    def test_only_with_letters_from_one_button(self):
        message = "abc"

        res = message_into_numbers(message)

        self.assertEqual(res, [2, -1, 2, 2, -1, 2, 2, 2])

    def test_with_capital_letters(self):
        message = "PyThOn"

        res = message_into_numbers(message)

        self.assertEqual(res, [1, 7, 9, 9, 9, 1, 8, 4, 4, 1, 6, 6, 6, 6, 6])

    def test_with_repeating_letters(self):
        message = "aabbcc"

        res = message_into_numbers(message)

        self.assertEqual(res, [2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2])


if __name__ == '__main__':
    unittest.main()
