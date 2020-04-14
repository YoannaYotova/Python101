import unittest
from change_precision import change_precision, ChangePrecision
from decimal import *


class TestChangePrecisionContextManagaer(unittest.TestCase):
    def test_change_precision_passes_with_correct_precision(self):
        with change_precision(2):
            res = Decimal('1.123132132') + Decimal('2.23232')

        self.assertEqual(res, Decimal('3.4'))

    def test_not_change_precision_outside_context_managaer(self):
        with change_precision(2):
            res1 = Decimal('1.123132132') + Decimal('2.23232')

        res2 = Decimal('1.123132132') + Decimal('2.23232')

        self.assertEqual(res1, Decimal('3.4'))
        self.assertEqual(res2, Decimal('3.355452132'))

    def test_change_precision_with_more_decimals(self):
        with change_precision(2):
            res1 = Decimal('3.12332112') + Decimal('2.23232')
            res2 = Decimal('1.123132132') + Decimal('5.03232')

        self.assertEqual(res1, Decimal('5.4'))
        self.assertEqual(res2, Decimal('6.2'))


class TestChangePrecisionClass(unittest.TestCase):
    def test_change_precision_passes_with_correct_precision(self):
        with ChangePrecision(2):
            res = Decimal('1.123132132') + Decimal('2.23232')

        self.assertEqual(res, Decimal('3.4'))

    def test_not_change_precision_outside_context_managaer(self):
        with ChangePrecision(2):
            res1 = Decimal('1.123132132') + Decimal('2.23232')

        res2 = Decimal('1.123132132') + Decimal('2.23232')

        self.assertEqual(res1, Decimal('3.4'))
        self.assertEqual(res2, Decimal('3.355452132'))

    def test_change_precision_with_more_decimals(self):
        with ChangePrecision(2):
            res1 = Decimal('3.12332112') + Decimal('2.23232')
            res2 = Decimal('1.123132132') + Decimal('5.03232')

        self.assertEqual(res1, Decimal('5.4'))
        self.assertEqual(res2, Decimal('6.2'))


if __name__ == '__main__':
    unittest.main()
