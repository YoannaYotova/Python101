import unittest
from frog_jumps import legal_moves


class TestLegalMoves(unittest.TestCase):
    def test_legal_moves_with_started_position(self):
        lake = '>>>_<<<'
        res = legal_moves(lake)

        expected = ['>>_><<<', '>_>><<<', '>>><_<<', '>>><<_<']

        self.assertEqual(res, expected)

    def test_legal_moves_with_not_the_started_position(self):
        lake = '>>_><<<'
        res = legal_moves(lake)

        lake2 = '>>><_<<'
        res2 = legal_moves(lake2)

        expected = ['>_>><<<', '_>>><<<', '>><>_<<']
        expected2 = ['>>_<><<', '>>><<_<', '>>><<<_']

        self.assertEqual(res, expected)
        self.assertEqual(res2, expected2)

    def test_legal_moves_with_not_the_started_position_and_cant_take_other_moves(self):
        lake = '_>>><<<'
        res = legal_moves(lake)

        lake2 = '<_>><'
        res2 = legal_moves(lake2)

        expected = []
        expected2 = []

        self.assertEqual(res, expected)
        self.assertEqual(res2, expected2)

    def test_legal_moves_with_not_the_started_position_and_shuffled_frogs(self):
        lake = '><><_'
        res = legal_moves(lake)

        lake2 = '><_<>'
        res2 = legal_moves(lake2)

        expected = ['><_<>']
        expected2 = ['_<><>', '><<_>']

        self.assertEqual(res, expected)
        self.assertEqual(res2, expected2)


if __name__ == '__main__':
    unittest.main()
