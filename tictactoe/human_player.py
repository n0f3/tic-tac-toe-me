from .base_player import BasePlayer
from .board import Board, BoardCellState, WinState
from math import floor


class HumanPlayer(BasePlayer):
    def make_move(self, board: Board) -> None:
        pos = -1
        valid_input = False
        coordinates = (-1, -1)

        while not valid_input:
            while pos not in range(1, 10):
                pos = input(
                    "Choose a position from 1 to 9 (top left is 1, bottom right is 9, left to right): "
                )
                if pos.isdigit():
                    pos = int(pos)
            coordinate_index = pos - 1
            coordinates = (
                floor(coordinate_index / 3),
                coordinate_index % 3,
            )
            if not board.check_cell_empty(coordinates=coordinates):
                print("Cell isn't empty! Select a different one")
                pos = -1
            else:
                valid_input = True

        x, y = coordinates
        cell = board.board[x * board.width + y]
        cell.state = BoardCellState.PLAYER

        # check if we win with this move
        self.win = (
            board.evaluate_win(cell=cell, state=BoardCellState.PLAYER)
            is WinState.PLAYER
        )
