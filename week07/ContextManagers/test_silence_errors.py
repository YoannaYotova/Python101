import unittest
from silence_errors import silence_errors, SilenceErrors


class TestSilenceErrorsContextManager(unittest.TestCase):
    def test_silence_passed_exception(self):
        exc = None
        try:
            with silence_errors(ValueError):
                raise ValueError('Test')
        except Exception as err:
            exc = err

        self.assertIsNone(exc)

    def test_silence_with_different_exception_from_passed_one(self):
        with self.assertRaises(ValueError):
            with silence_errors(TypeError):
                raise ValueError('Test')

    def test_not_silences_passed_exception_outside_context_manager(self):
        with self.assertRaises(ValueError, msg='Testing outside the with block'):
            with silence_errors(TypeError):
                raise ValueError('Testing inside the with block')

            raise ValueError('Testing inside the with block')

    def test_silence_passed_with_same_exception_and_same_message(self):
        exc = None
        msg = 'Testing with message'

        try:
            with silence_errors(ValueError, message=msg):
                raise ValueError(msg)
        except Exception as e:
            exc = e

        self.assertIsNone(exc)

    def test_not_silence_passed_with_same_exception_and_different_message(self):
        msg = 'Testing with message'

        with self.assertRaises(ValueError):
            with silence_errors(ValueError, message=msg):
                raise ValueError('Different message')

    def test_not_silence_passed_with_different_exception_and_same_message(self):
        msg = 'Testing with message'

        with self.assertRaises(ValueError):
            with silence_errors(TypeError, message=msg):
                raise ValueError(msg)


class TestSilenceErrorsClass(unittest.TestCase):
    def test_silence_passed_exception(self):
        exc = None
        try:
            with SilenceErrors(ValueError):
                raise ValueError('Test')
        except Exception as err:
            exc = err

        self.assertIsNone(exc)

    def test_silence_with_different_exception_from_passed_one(self):
        with self.assertRaises(ValueError):
            with SilenceErrors(TypeError):
                raise ValueError('Test')

    def test_not_silences_passed_exception_outside_context_manager(self):
        with self.assertRaises(ValueError, msg='Testing outside the with block'):
            with SilenceErrors(TypeError):
                raise ValueError('Testing inside the with block')

            raise ValueError('Testing inside the with block')

    def test_silence_passed_with_same_exception_and_same_message(self):
        exc = None
        msg = 'Testing with message'

        try:
            with SilenceErrors(ValueError, message=msg):
                raise ValueError(msg)
        except Exception as e:
            exc = e

        self.assertIsNone(exc)

    def test_not_silence_passed_with_same_exception_and_different_message(self):
        msg = 'Testing with message'

        with self.assertRaises(ValueError):
            with SilenceErrors(ValueError, message=msg):
                raise ValueError('Different message')

    def test_not_silence_passed_with_different_exception_and_same_message(self):
        msg = 'Testing with message'

        with self.assertRaises(ValueError):
            with SilenceErrors(TypeError, message=msg):
                raise ValueError(msg)


if __name__ == '__main__':
    unittest.main()
