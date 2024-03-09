from .constants import PLAYER, Tile
from .exceptions import Invalid2dIndexException, \
    TileAtIndexAlreadyOccupiedException
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
        error_message: str = ""
        while True:
            try:
                if error_message != "":
                    print(error_message)
                i1d = ttt_get_valid_1d_index(f"{turn}>")
                if i1d == -1:
                    return (0, 0)
                ix2d, iy2d = ttt_convert_1d_to_2d(i1d)
                ttt_validate_tile_place_attempt(board, ix2d, iy2d)
                board[iy2d][ix2d] = turn
            except Invalid2dIndexException:
                error_message = "This position does not exist!"
                continue
            except TileAtIndexAlreadyOccupiedException:
                error_message = "This position is already occupied!"
                continue
            except Exception as e:
                raise e
            break
        turn = ttt_get_opposite_turn(turn)
        print()
