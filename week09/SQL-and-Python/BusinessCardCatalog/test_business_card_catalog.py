import unittest
from unittest.mock import patch
from business_card_catalog import add


class TestAdd(unittest.TestCase):
    @patch('business_card_catalog.input', side_effect=['yoanna', 'yonibonboni@gmail.com', 23, '0882313123', 'something'])
    def test_add_values_into_databases(self, input_mock):
        add()


if __name__ == '__main__':
    unittest.main()
