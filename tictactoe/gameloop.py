from .helper import ask_confirm
from .tictactoe import ttt_game


def ttt_gameloop() -> tuple[int, int]:
    """
    Return Value
    :returns: (score of the player, score of the computer)
    """
    score_player: int = 0
    score_computer: int = 0
    while True:
        res = ttt_game()
        score_player += res[0]
        score_computer += res[1]
        continue_ = ask_confirm("Continue? ")
        if not continue_:
            break
    return (score_player, score_computer)
