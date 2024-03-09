from unittest import TestCase
from ..constants import EMPTY, PLAYER, COMPUTER
from ..exceptions import Invalid2dIndexException, \
    TileAtIndexAlreadyOccupiedException
from ..helper import ttt_generate_board, ttt_validate_tile_place_attempt, \
    ttt_are_moves_remaining, ttt_get_opposite_turn, ttt_convert_1d_to_2d


# ===========================
# The TicTacToe board
# ===========================


class TestAreMovesRemaining(TestCase):
    def test_empty_board(self):
        b = ttt_generate_board()
        res = ttt_are_moves_remaining(b)
        self.assertTrue(res)

    def test_not_full_board(self):
        b = ttt_generate_board(PLAYER)
        b[2][2] = EMPTY
        res = ttt_are_moves_remaining(b)
        self.assertTrue(res)

    def test_full_board(self):
        b = ttt_generate_board(PLAYER)
        res = ttt_are_moves_remaining(b)
        self.assertFalse(res)


# ===========================
# Game utilities and math
# ===========================


class TestValidateTilePlaceAttempt(TestCase):
    def test_index_to_small(self):
        b = ttt_generate_board()
        try:
            ttt_validate_tile_place_attempt(b, -1, -1)
        except Invalid2dIndexException:
            return
        raise Exception()

    def test_index_to_big(self):
        b = ttt_generate_board()
        try:
            ttt_validate_tile_place_attempt(b, 3, 3)
        except Invalid2dIndexException:
            return
        raise Exception()

    def test_index_is_occupied(self):
        b = ttt_generate_board()
        b[1][1] = PLAYER
        try:
            ttt_validate_tile_place_attempt(b, 1, 1)
        except TileAtIndexAlreadyOccupiedException:
            return
        raise Exception()

    def test_everything_fine(self):
        b = ttt_generate_board()
        ttt_validate_tile_place_attempt(b, 0, 0)


class TestGetOppositeTurn(TestCase):
    def test_player_to_computer(self):
        res = ttt_get_opposite_turn(PLAYER)
        self.assertEqual(res, COMPUTER)

    def test_computer_to_player(self):
        res = ttt_get_opposite_turn(COMPUTER)
        self.assertEqual(res, PLAYER)


class TestConvert1dTo2d(TestCase):
    def test_index_first_tile(self):
        res = ttt_convert_1d_to_2d(0)
        self.assertEqual(res, (0, 0))

    def test_index_second_tile(self):
        res = ttt_convert_1d_to_2d(1)
        self.assertEqual(res, (1, 0))

    def test_index_center_tile(self):
        res = ttt_convert_1d_to_2d(4)
        self.assertEqual(res, (1, 1))

    def test_index_last_tile(self):
        res = ttt_convert_1d_to_2d(8)
        self.assertEqual(res, (2, 2))
