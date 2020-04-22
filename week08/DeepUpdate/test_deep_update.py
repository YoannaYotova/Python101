import unittest
from deep_update import deep_update


class TestDeepUpdate(unittest.TestCase):
        def test_deep_update_with_dictionary_with_one_occurance_of_the_given_key(self):
            root = {
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

            deep_update(root, 'aa', 'Yoana')

            expected = {
                'a': {
                    'aa': 'Yoana',
                    'aaa': {
                        'ani': 23,
                        'pesho': ['p', 'e', 's', 'h', 'o']
                    }
                },
                'b': 2,
                'c': 3
            }
            self.assertEqual(root, expected)

        def test_deep_update_with_dictionary_with_more_occurance_of_the_given_key(self):
            root = {
                'a': {
                    'aa': 2,
                    'aaa': {
                        'ani': 23,
                        'pesho': ['p', 'e', 's', 'h', 'o']
                    }
                },
                'aa': 'bau',
                'b': 2,
                'c': 3
            }

            deep_update(root, 'aa', 'Yoana')

            expected = {
                'a': {
                    'aa': 'Yoana',
                    'aaa': {
                        'ani': 23,
                        'pesho': ['p', 'e', 's', 'h', 'o']
                    }
                },
                'aa': 'Yoana',
                'b': 2,
                'c': 3
            }
            self.assertEqual(root, expected)

        def test_deep_update_with_dictionary_and_list_of_dictionaries(self):
            root = {
                'a': {
                    'aa': 2,
                    'aaa': {
                        'ani': 23,
                        'pesho': ['p', 'e', 's', 'h', 'o']
                    }
                },
                'b': [{'name': 'Anni', 'year': 23, 'color': 'blue'}, {'name': 'Pesho', 'year': 25, 'color': 'yellow'}],
                'c': 3,
                'color': 'purple'
            }

            deep_update(root, 'color', 'red')

            expected = {
                'a': {
                    'aa': 2,
                    'aaa': {
                        'ani': 23,
                        'pesho': ['p', 'e', 's', 'h', 'o']
                    }
                },
                'b': [{'name': 'Anni', 'year': 23, 'color': 'red'}, {'name': 'Pesho', 'year': 25, 'color': 'red'}],
                'c': 3,
                'color': 'red'
            }

            self.assertEqual(root, expected)


if __name__ == '__main__':
    unittest.main()
