from .constants import PLAYER, COMPUTER, EMPTY, Tile, Board
from .exceptions import Invalid2dIndexException, \
    TileAtIndexAlreadyOccupiedException

# ===========================
# User input
# ===========================


def ask_confirm(msg: str = "") -> bool:
    s: str = input(msg).strip()
    return s == "" or s[0] == "y" or s[0] == "Y"


def ttt_get_valid_1d_index(msg: str = "") -> int:
    while True:
        try:
            i = int(input(msg).strip())
            if i == -1:
                return i
            return i - 1
        except ValueError:
            continue
        except Exception as e:
            raise e


# ===========================
# The TicTacToe board
# ===========================


def ttt_generate_board(sym: Tile = EMPTY) -> Board:
    """Get an empty 3x3 TicTacToe board."""
    return (
        [sym, sym, sym],
        [sym, sym, sym],
        [sym, sym, sym]
    )


def ttt_print_board(b: Board):
    """Print an 3x3 TicTacToe board to `stdout`."""
    for y in range(3):
        for x in range(3):
            print(b[y][x], end="")
        print()


def ttt_validate_tile_place_attempt(board: Board, x: int, y: int):
    """
    Raises `Invalid2dIndexException` if the index is out of bound.
    Raises `TileAtIndexAlreadyOccupiedException` if the index is not empty.
    """
    if not 0 <= x <= 2 or not 0 <= y <= 2:
        raise Invalid2dIndexException(
            f"Argument x or y is to big/small. x={x} y={x}")
    if board[y][x] != EMPTY:
        raise TileAtIndexAlreadyOccupiedException(
            "The tile at board[{y}][{x}] does not equal EMPTY.")


def ttt_are_moves_remaining(board: Board) -> bool:
    for y in range(3):
        for x in range(3):
            if board[y][x] == EMPTY:
                return True
    return False


def ttt_get_available_moves(board: Board) -> list[tuple[int, int]]:
    """Returns [(x, y), (x, y), ...]"""
    available_moves: list[tuple[int, int]] = []
    for y in range(3):
        for x in range(3):
            if board[y][x] == EMPTY:
                available_moves.append((x, y))
    return available_moves


# ===========================
# Check for winner
# ===========================


def ttt_check_winner(board: Board) -> Tile | None:
    # Vertical and horizontal
    for yx in range(3):
        # Horizontal
        if board[yx][0] == board[yx][1] == board[yx][2] != EMPTY:
            return board[yx][0]
        # Vertical
        if board[0][yx] == board[1][yx] == board[2][yx] != EMPTY:
            return board[0][yx]

    # Diagonal
    if board[1][1] != EMPTY and (
        board[0][0] == board[1][1] == board[2][2] or
        board[0][2] == board[1][1] == board[2][0]
    ):
        return board[1][1]

    # Tie
    if not ttt_are_moves_remaining(board):
        return None

    # Game still going
    return EMPTY


# ===========================
# Game utilities and math
# ===========================


def ttt_get_opposite_turn(turn_now: Tile) -> Tile:
    return PLAYER if turn_now == COMPUTER else COMPUTER


def ttt_convert_1d_to_2d(i1d: int) -> tuple[int, int]:
    """Returns (x, y)."""
    return (i1d % 3, i1d // 3)
