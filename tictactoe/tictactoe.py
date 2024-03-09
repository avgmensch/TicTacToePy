from .helper import ttt_generate_board, ttt_print_board


def ttt_game() -> tuple[int, int]:
    """
    Return Value
    :returns: (1 if player wins else 0, same for computer)
    """
    board = ttt_generate_board()
    while True:
        ttt_print_board(board)
        break
    return (0, 0)
