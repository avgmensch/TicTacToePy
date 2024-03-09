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
        sum_ = sum(res)
        if sum_ >= 0:
            score_player += res[0]
            score_computer += res[1]
        else:
            print()
        print(f"Player:   {score_player}\nComputer: {score_computer}")
        if sum_ >= 0:
            continue_ = ask_confirm("Continue? ")
            if continue_:
                print()
                continue
        break
    return (score_player, score_computer)
