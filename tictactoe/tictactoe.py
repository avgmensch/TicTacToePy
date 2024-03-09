from .constants import PLAYER, Tile
from .helper import ttt_get_valid_1d_index, ttt_generate_board, \
    ttt_print_board, ttt_validate_tile_place_attempt, ttt_get_opposite_turn, ttt_convert_1d_to_2d


def ttt_game() -> tuple[int, int]:
    """
    Return Value
    :returns: (1 if player wins else 0, same for computer)
    """
    board = ttt_generate_board()
    turn: Tile = PLAYER
    while True:
        ttt_print_board(board)
        i1d = ttt_get_valid_1d_index(f"{turn}>")
        if i1d == -1:
            return (0, 0)
        ix2d, iy2d = ttt_convert_1d_to_2d(i1d)
        ttt_validate_tile_place_attempt(board, ix2d, iy2d) #TODO: try/catch
        board[iy2d][ix2d] = turn
        turn = ttt_get_opposite_turn(turn)
