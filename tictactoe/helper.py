from .constants import EMPTY, Board

# ===========================
# User input
# ===========================


def ask_confirm(msg: str = "") -> bool:
    s: str = input(msg).strip()
    return s == "" or s[0] == "y" or s[0] == "Y"


# ===========================
# The TicTacToe board
# ===========================


def ttt_generate_board() -> Board:
    """Get an empty 3x3 TicTacToe board."""
    return (
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    )


def ttt_print_board(b: Board):
    """Print an 3x3 TicTacToe board to `stdout`."""
    for y in range(3):
        for x in range(3):
            print(b[y][x], end="")
        print()
