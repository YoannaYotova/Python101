import unittest
from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):
    def test_with_empty_list_raise_error(self):
        exc = None

        try:
            BowlingGame.validate([])
        except Exception as err:
            exc = err

        self.assertIsNotNone(str(exc))
        self.assertEqual(str(exc), 'Invalid number of frames')

    def test_with_invalid_numbers_of_frames_raise_error(self):
        exc = None

        try:
            BowlingGame.validate([5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6])
        except Exception as err:
            exc = err

        self.assertIsNotNone(str(exc))
        self.assertEqual(str(exc), 'Invalid number of frames')

    def test_with_invalid_numbers_of_frames_with_strike_not_in_the_tenth_frame_raise_error(self):
        exc = None

        try:
            BowlingGame.validate([5, 1, 10, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        except Exception as err:
            exc = err

        self.assertIsNotNone(str(exc))
        self.assertEqual(str(exc), 'Invalid number of frames')

    def test_return_true_if_it_is_strike(self):
        game = BowlingGame([3, 1, 10, 3, 2, 3, 5, 1, 1, 0, 1, 2, 3, 1, 4, 3, 2, 1, 6])

        res = game._is_strike(2)

        self.assertEqual(res, True)

    def test_return_true_if_it_is_not_strike(self):
        game = BowlingGame([3, 1, 7, 3, 2, 3, 5, 1, 1, 0, 1, 2, 3, 1, 4, 3, 2, 1, 6, 1])

        res = game._is_strike(2)

        self.assertEqual(res, False)

    def test_return_true_if_it_is_spare(self):
        game = BowlingGame([3, 1, 7, 3, 2, 3, 5, 1, 1, 0, 1, 2, 3, 1, 4, 3, 2, 1, 6, 1])

        res = game._is_spare(3)

        self.assertEqual(res, True)

    def test_return_true_if_it_is_not_spare(self):
        game = BowlingGame([3, 1, 2, 3, 2, 3, 5, 1, 1, 0, 1, 2, 3, 1, 4, 3, 2, 1, 6, 1])

        res = game._is_spare(3)

        self.assertEqual(res, False)

    def test_given_index_from_differen_frames_return_false(self):
        game = BowlingGame([3, 1, 7, 3, 2, 3, 5, 1, 1, 0, 1, 2, 3, 1, 4, 3, 2, 1, 6, 1])

        res = game._is_spare(2)

        self.assertEqual(res, False)

    def test_result_if_there_are_no_strikes_and_spares(self):
        game = BowlingGame([1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2])

        res = game.result()

        self.assertEqual(res, 65)

    def test_result_if_there_is_one_strike(self):
        game = BowlingGame([1, 4, 10, 1, 2, 3, 5, 1, 1, 0, 1, 2, 3, 1, 4, 3, 2, 1, 6])

        res = game.result()

        self.assertEqual(res, 54)

    def test_result_if_there_are_many_strikes(self):
        game = BowlingGame([1, 4, 10, 1, 2, 10, 1, 1, 1, 0, 10, 1, 2, 1, 1, 1, 1])

        res = game.result()

        self.assertEqual(res, 56)

    def test_result_if_there_are_many_strikes_in_a_row(self):
        game = BowlingGame([1, 4, 10, 10, 2, 1, 1, 1, 1, 0, 10, 1, 2, 1, 1, 1, 1])

        res = game.result()

        self.assertEqual(res, 66)

    def test_result_if_there_are_only_strikes_in_a_row(self):
        game = BowlingGame([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])

        res = game.result()

        self.assertEqual(res, 300)

    def test_result_if_there_is_one_stpare(self):
        game = BowlingGame([1, 4, 1, 2, 5, 5, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        res = game.result()

        self.assertEqual(res, 21)

    def test_result_if_there_are_many_stpares(self):
        game = BowlingGame([6, 4, 0, 0, 3, 7, 3, 0, 5, 5, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])

        res = game.result()

        self.assertEqual(res, 39)

    def test_result_if_there_are_many_stpares_in_a_row(self):
        game = BowlingGame([6, 4, 3, 7, 3, 0, 5, 5, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        res = game.result()

        self.assertEqual(res, 42)

    def test_result_if_there_is_a_strike_in_the_tenth_frame(self):
        game = BowlingGame([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 1])

        res = game.result()

        self.assertEqual(res, 30)

    def test_result_if_there_is_a_spare_in_the_tenth_frame(self):
        game = BowlingGame([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 1])

        res = game.result()

        self.assertEqual(res, 29)


if __name__ == '__main__':
    unittest.main()
