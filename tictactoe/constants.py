from typing import Literal, Tuple, List

PLAYER = "X"
COMPUTER = "O"
EMPTY = "-"

Tile = Literal["X", "O", "-"]
"""Represent a Tile on a TicTacToe board."""

Board = Tuple[List[Tile], List[Tile], List[Tile]]
"""Represent a 3x3 TicTacToe board consisting of `Tile`s."""
