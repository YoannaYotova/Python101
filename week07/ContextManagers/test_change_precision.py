import unittest
from change_precision import change_precision
from decimal import *


class TestChangePrecision(unittest.TestCase):
    def test_change_precision(self):
        with change_precision(3):
            res = Decimal('1.0213455324') + Decimal('2.231234')

        self.assertEqual(res, Decimal('3.25'))


if __name__ == '__main__':
    unittest.main()
