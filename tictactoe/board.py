from enum import Enum, auto
from typing import Optional, Iterator
from random import choice
from math import floor
from .board_cell import BoardCell, BoardCellState


class WinState(Enum):
    DRAW = 0
    AI = 10
    PLAYER = -10


class WinCondition(Enum):
    ROW = auto()
    COLUMN = auto()
    MAIN_DIAGONAL = auto()
    OPPOSITE_DIAGONAL = auto()


class Board:
    def __init__(self, player_symbol: str, ai_symbol: str) -> None:
        self.board_size = 9
        self.width = 3
        self.height = 3
        self.board = [
            BoardCell(
                position=(floor(index / 3), index % 3),
                player_symbol=player_symbol,
                ai_symbol=ai_symbol,
            )
            for index in range(self.board_size)
        ]

    def __str__(self) -> str:
        formatted = "----------\n"
        for index in range(self.board_size):
            formatted += str(self.board[index])
            if (index + 1) % 3 == 0:
                formatted += "\n----------\n"
            else:
                formatted += " | "
        return formatted

    def moves_left(self) -> bool:
        for cell in self.board:
            if cell.state is BoardCellState.EMPTY:
                return True
        return False

    def assign_move(self, coordinates: (int, int), state: BoardCellState) -> None:
        x, y = coordinates
        self.board[x * self.width + y].state = state

    def check_cell_empty(self, coordinates: (int, int)) -> bool:
        x, y = coordinates
        return self.board[x * self.width + y].state is BoardCellState.EMPTY

    def reset(self) -> None:
        for cell in self.board:
            cell.state = BoardCellState.EMPTY

    def check_row_for_win(
        self,
        row: int,
        state: BoardCellState,
        win_result: WinState,
    ) -> Optional[WinState]:
        for index in range(self.width):
            if self.board[row * self.width + index].state != state:
                return None
            if index == self.width - 1:
                return win_result

    def check_column_for_win(
        self, column: int, state: BoardCellState, win_result: WinState
    ) -> Optional[WinState]:
        for index in range(self.width):
            if self.board[index * self.width + column].state != state:
                return None
            if index == self.width - 1:
                return win_result

    def check_main_diagonal_for_win(
        self, state: BoardCellState, win_result: WinState
    ) -> Optional[WinState]:
        for index in range(self.width):
            if self.board[index * self.width + index].state != state:
                return None
            if index == self.width - 1:
                return win_result

    def check_opposite_diagonal_for_win(
        self, state: BoardCellState, win_result: WinState
    ) -> Optional[WinState]:
        for index in range(self.width):
            if self.board[index * self.width + self.width - 1 - index].state != state:
                return None
            if index == self.width - 1:
                return win_result

    def evaluate_win(self, cell: BoardCell, state: BoardCellState) -> WinState:
        win_result = WinState.AI if state is BoardCellState.AI else WinState.PLAYER

        x, y = cell.position
        is_main_diagonal = x == y
        is_opposite_diagonal = x + y == self.width - 1

        row_win = self.check_row_for_win(row=x, state=state, win_result=win_result)
        if row_win:
            return row_win

        column_win = self.check_column_for_win(
            column=y, state=state, win_result=win_result
        )

        if column_win:
            return column_win

        # check diagonals
        if is_main_diagonal:
            main_diagonal_win = self.check_main_diagonal_for_win(
                state=state, win_result=win_result
            )
            if main_diagonal_win:
                return main_diagonal_win

        if is_opposite_diagonal:
            opposite_diagonal_win = self.check_opposite_diagonal_for_win(
                state=state, win_result=win_result
            )
            if opposite_diagonal_win:
                return opposite_diagonal_win

        return WinState.DRAW

    def get_empty_cells(self) -> Iterator[BoardCell]:
        return filter(lambda cell: cell.state is BoardCellState.EMPTY, self.board)

    def get_random_empty(self) -> Optional[BoardCell]:
        empty_cells = list(self.get_empty_cells())
        return choice(empty_cells) if len(empty_cells) > 0 else None
