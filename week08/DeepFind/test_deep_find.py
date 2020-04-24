import unittest
from deep_find import deep_find, deep_find_dfs, deep_find_bfs


class TestDeepFind(unittest.TestCase):
    def test_deep_find_recursion_with_simple_dictionary_and_no_occurances(self):
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

        res = deep_find(root, 'Anni')

        self.assertIsNone(res)

    def test_deep_find_recursion_with_simple_dictionary(self):
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

        res = deep_find(root, 'aa')

        self.assertEqual(res, 2)

    def test_deep_find_recursion_with_more_dictionaries(self):
        root = {
            'a': {
                'aa': 2,
                'aaa': {
                    'ani': 23,
                    'pesho': ['p', 'e', 's', 'h', 'o']
                }
            },
            'pets': {'doggy': 2, 'names': ['jeny', 'peny']},
            'b': 2,
            'c': 3
        }

        res = deep_find(root, 'doggy')

        self.assertEqual(res, 2)

    def test_deep_find_recursion_with_list_of_dictionaries(self):
        root = {
            'a': {
                'aa': 2,
                'aaa': {
                    'ani': 23,
                    'pesho': ['p', 'e', 's', 'h', 'o']
                }
            },
            'pets': [{'doggy': 2, 'names': ['jeny', 'peny']}, {'catty': 2, 'names': ['kitty', 'missy']}],
            'b': 2,
            'c': 3
        }

        res = deep_find(root, 'doggy')

        self.assertEqual(res, 2)


class TestDeepFindDFS(unittest.TestCase):
    def test_deep_find_dfs_with_simple_dictionary_and_no_occurances(self):
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

        res = deep_find_dfs(root, 'Anni')

        self.assertIsNone(res)

    # # TODO
    def test_deep_find_dfs_with_simple_dictionary(self):
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

        res = deep_find_dfs(root, 'ani')

        self.assertEqual(res, 23)

    def test_deep_find_dfs_with_more_occurances_in_the_dictionary_returns_first_occurance(self):
        root = {
            'a': {
                'aa': 2,
                'aaa': {
                    'ani': 23,
                    'pesho': ['p', 'e', 's', 'h', 'o']
                }
            },
            'aa': ['doggy', 'catty'],
            'b': 2,
            'c': 3
        }

        res = deep_find_dfs(root, 'aa')

        self.assertEqual(res, ['doggy', 'catty'])

    def test_deep_find_dfs_with_one_occurance_in_the_dictionary_with_list_of_dictionaries(self):
        root = {
            'a': {
                'aa': 2,
                'aaa': {
                    'ani': 23,
                    'pesho': ['p', 'e', 's', 'h', 'o']
                }
            },
            'aa': [{'doggy': 2, 'names': ['jeny', 'peny']}, {'catty': 2, 'names': ['kitty', 'missy']}],
            'b': 2,
            'c': 3
        }

        res = deep_find_dfs(root, 'doggy')

        self.assertEqual(res, 2)


class TestDeepFindBFS(unittest.TestCase):
    def test_deep_find_bfs_with_simple_dictionary_and_no_occurances(self):
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

        res = deep_find_bfs(root, 'Anni')

        self.assertIsNone(res)

    def test_deep_find_bfs_with_simple_dictionary(self):
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

        res = deep_find_bfs(root, 'aa')

        self.assertEqual(res, 2)

    def test_deep_find_bfs_with_more_occurances_in_the_dictionary_returns_first_occurance(self):
        root = {
            'a': {
                'aa': 2,
                'aaa': {
                    'ani': 23,
                    'pesho': ['p', 'e', 's', 'h', 'o']
                }
            },
            'aa': ['doggy', 'catty'],
            'b': 2,
            'c': 3
        }

        res = deep_find_bfs(root, 'aa')

        self.assertEqual(res, 2)

    def test_deep_find_bfs_with_one_occurance_in_the_dictionary_with_list_of_dictionaries(self):
        root = {
            'a': {
                'aa': 2,
                'aaa': {
                    'ani': 23,
                    'pesho': ['p', 'e', 's', 'h', 'o']
                }
            },
            'aa': [{'doggy': 2, 'names': ['jeny', 'peny']}, {'catty': 2, 'names': ['kitty', 'missy']}],
            'b': 2,
            'c': 3
        }

        res = deep_find_bfs(root, 'doggy')

        self.assertEqual(res, 2)


if __name__ == '__main__':
    unittest.main()
