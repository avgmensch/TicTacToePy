from .constants import PLAYER, COMPUTER, Tile, Board
from .helper import ttt_get_available_moves, ttt_check_winner, ttt_get_opposite_turn


def minimax(board: Board, turn: Tile, depth: int = 0) -> int:
    # TODO: Use depth
    if turn != PLAYER and turn != COMPUTER:
        raise Exception()  # TODO: Create actual exception

    winner = ttt_check_winner(board)
    if winner == PLAYER:
        return depth - 10
    elif winner == COMPUTER:
        return 10 - depth
    elif winner is None:
        return 0

    # [(x, y), (x, y), ...]
    available_moves = ttt_get_available_moves(board)

    # Minimizer
    if turn == PLAYER:
        best_score = 99
        for x, y in available_moves:
            old = board[y][x]
            board[y][x] = PLAYER
            s = minimax(board, COMPUTER, depth+1)
            best_score = min(s, best_score)
            board[y][x] = old
        return best_score

    # Maximizer
    elif turn == COMPUTER:
        best_score = -99
        for x, y in available_moves:
            old = board[y][x]
            board[y][x] = COMPUTER
            s = minimax(board, PLAYER, depth+1)
            best_score = max(s, best_score)
            board[y][x] = old
        return best_score

    else:
        raise Exception()  # TODO: Create actual exception


def ttt_get_best_move(board: Board, turn: Tile) -> tuple[int, int]:
    """Returns (x, y)"""
    if turn != PLAYER and turn != COMPUTER:
        raise Exception()  # TODO: Create actual exception

    best_move: tuple[int, int] = (0, 0)
    best_score: int = 99 if turn == PLAYER else -99
    available_moves = ttt_get_available_moves(board)

    for x, y in available_moves:
        old = board[y][x]
        board[y][x] = turn
        s = minimax(board, ttt_get_opposite_turn(turn))
        board[y][x] = old
        if (
            (turn == PLAYER and s < best_score) or
            (turn == COMPUTER and s > best_score)
        ):
            best_score = s
            best_move = (x, y)

    return best_move
