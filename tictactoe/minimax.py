from .constants import PLAYER, COMPUTER, Tile, Board
from .helper import ttt_get_available_moves, ttt_check_winner


def minimax(board: Board, turn: Tile, depth: int = 0) -> int:
    if turn != PLAYER and turn != COMPUTER:
        raise Exception()  # TODO: Create actual exception

    winner = ttt_check_winner(board)
    if winner == PLAYER:
        return -10
    elif winner == COMPUTER:
        return 10
    elif winner is None:
        return 0

    # [(x, y), (x, y), ...]
    available_moves = ttt_get_available_moves(board)

    if turn == PLAYER:
        best_score = 99
        for x, y in available_moves:
            old = board[y][x]
            board[y][x] = PLAYER
            s = minimax(board, COMPUTER, depth+1)
            best_score = min(s, best_score)
            board[y][x] = old
        return best_score

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
