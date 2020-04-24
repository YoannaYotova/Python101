import unittest
from deep_apply import deep_apply, func

class TestDeepApply(unittest.TestCase):
    def test_deep_apply_with_simple_dictionary_and_all_keys_are_strings(self):
        root = {
            'a': {
                'aa': 2,
                'aaa': 42
            },
            'b': 2,
            'c': 3
        }

        res = deep_apply(func, root)

        excpected = {
            'a_new':{
                'aa_new': 2,
                'aaa_new': 42
            },
            'b_new': 2,
            'c_new': 3
        }

        self.assertEqual(res, excpected)

    def test_deep_apply_with_nested_dictionaries_and_all_keys_are_strings(self):
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

        res = deep_apply(func, root)

        excpected = {
            'a_new': {
                'aa_new': 2,
                'aaa_new': {
                    'ani_new': 23,
                    'pesho_new': ['p', 'e', 's', 'h', 'o']
                }
            },
            'pets_new': {'doggy_new': 2, 'names_new': ['jeny', 'peny']},
            'b_new': 2,
            'c_new': 3
        }

        self.assertEqual(res, excpected)

    def test_deep_apply_with_nested_dictionaries_and_different_types_of_keys_wich_are_imutable(self):
        root = {
            1: {
                'aa': 2,
                'aaa': {
                    'ani': 23,
                    'pesho': ['p', 'e', 's', 'h', 'o']
                }
            },
            2: {'doggy': 2, 'names': ['jeny', 'peny']},
            3: 2,
            4: 3
        }

        res = deep_apply(func, root)

        excpected = {
            '1_new': {
                'aa_new': 2,
                'aaa_new': {
                    'ani_new': 23,
                    'pesho_new': ['p', 'e', 's', 'h', 'o']
                }
            },
            '2_new': {'doggy_new': 2, 'names_new': ['jeny', 'peny']},
            '3_new': 2,
            '4_new': 3
        }

        self.assertEqual(res, excpected)

if __name__ == '__main__':
    unittest.main()
