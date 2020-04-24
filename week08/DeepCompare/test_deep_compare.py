import unittest
from deep_compare import deep_compare

class TestDeepCompare(unittest.TestCase):
    def test_deep_compare_with_two_simple_dictionaries_wich_are_same_returns_true(self):
        obj1 = {
            'a': '133',
            'pets': [1,2,3],
            'b': 2,
            'c': 3
        }

        obj2 = {
            'a': '133',
            'pets': [1,2,3],
            'b': 2,
            'c': 3
        }

        res = deep_compare(obj1, obj2)

        self.assertEqual(res, True)

    def test_deep_compare_with_two_simple_dictionaries_which_are_different_returns_true(self):
        obj1 = {
            'a': '133',
            'pets': [1,2,3],
            'b': 2,
            'c': 3
        }

        obj2 = {
            'a': '133',
            'pets': [1,2],
            'b': 2,
            'c': 3
        }

        res = deep_compare(obj1, obj2)

        self.assertEqual(res, False)

    def test_deep_compare_with_two_nested_dictionaries_wich_are_same_returns_true(self):
        obj1 = {
            'a': {
                'aa': 2,
                'aaa': {
                    'ani': 23,
                    'pesho': ['p', 'e', 's', 'h', 'o']
                }
            },
            'b': 2,
            'c': 3
        }

        obj2 = {
            'a': {
                'aa': 2,
                'aaa': {
                    'ani': 23,
                    'pesho': ['p', 'e', 's', 'h', 'o']
                }
            },
            'b': 2,
            'c': 3
        }

        res = deep_compare(obj1, obj2)

        self.assertEqual(res, True)

    def test_deep_compare_with_two_nested_dictionaries_wich_are_different_returns_false(self):
        obj1 = {
            'a': {
                'aa': 2,
                'aaa': {
                    'ani': 23,
                    'pesho': ['p', 'e', 's', 'h', 'o']
                }
            },
            'b': 2,
            'c': 3
        }

        obj2 = {
            'a': {
                'aa': 2,
                'aaa': {
                    'ani': 231,
                    'pesho': ['p', 'e', 'c', 'h', 'o']
                }
            },
            'b': 2,
            'c': 3
        }

        res = deep_compare(obj1, obj2)

        self.assertEqual(res, False)

if __name__ == '__main__':
    unittest.main()
