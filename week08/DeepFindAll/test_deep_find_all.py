import unittest
from deep_find_all import deep_find_all_dfs, deep_find_all_bfs


class TestDeepFindAllDFS(unittest.TestCase):
    def test_find_all_whean_there_is_no_occurence(self):
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

        res = deep_find_all_dfs(root, 'Yoanna')

        self.assertEqual(res, [])

    def test_find_all_keys_with_simple_dictionary(self):
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

        res = deep_find_all_dfs(root, 'aa')

        self.assertEqual(res, [2])

    def test_deep_find_dfs_with_more_occurances_in_the_dictionary_returns_all_values(self):
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

        res = deep_find_all_dfs(root, 'aa')

        self.assertEqual(res, [['doggy', 'catty'], 2])

    def test_deep_find_dfs_with_more_occurances_in_the_dictionary_and_more_nested_structeres_returns_al_values(self):
        root = {
            'a': {
                'aa': 2,
                'aaa': {
                    'ani': 23,
                    'pesho': ['p', 'e', 's', 'h', 'o']
                },
                'ani': 'panda'
            },
            'aa': ['doggy', 'catty'],
            'ani': 'girl',
            'b': 2,
            'c': 3
        }

        res = deep_find_all_dfs(root, 'ani')

        self.assertEqual(res, ['girl', 'panda', 23 ])


class TestDeepFindAllBFS(unittest.TestCase):
    def test_find_all_whean_there_is_no_occurence(self):
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

        res = deep_find_all_bfs(root, 'Yoanna')

        self.assertEqual(res, [])

    def test_find_all_keys_with_simple_dictionary(self):
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

        res = deep_find_all_bfs(root, 'aa')

        self.assertEqual(res, [2])

    def test_deep_find_dfs_with_more_occurances_in_the_dictionary_returns_all_values(self):
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

        res = deep_find_all_bfs(root, 'aa')

        self.assertEqual(res, [['doggy', 'catty'], 2])

    def test_deep_find_dfs_with_more_occurances_in_the_dictionary_and_more_nested_structeres_returns_al_values(self):
        root = {
            'a': {
                'aa': 2,
                'aaa': {
                    'ani': 23,
                    'pesho': ['p', 'e', 's', 'h', 'o']
                },
                'ani': 'panda'
            },
            'aa': ['doggy', 'catty'],
            'ani': 'girl',
            'b': 2,
            'c': 3
        }

        res = deep_find_all_bfs(root, 'ani')

        self.assertEqual(res, ['girl', 'panda', 23])


if __name__ == '__main__':
    unittest.main()
