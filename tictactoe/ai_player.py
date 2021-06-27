import random
import sys

from .base_player import BasePlayer
from .board import Board, BoardCellState, WinState, BoardCell


class AIPlayer(BasePlayer):
    def find_best_move(self, board: Board) -> BoardCell:
        best_score = -sys.maxsize
        best_move = None

        depth = random.randint(2, 6)
        for cell in board.get_empty_cells():
            cell.state = BoardCellState.AI
            score = self.minimax(
                board=board,
                cell=cell,
                depth=depth,
                is_maximizing=False,
                alpha=-sys.maxsize,
                beta=sys.maxsize,
                state=BoardCellState.AI,
            )
            cell.state = BoardCellState.EMPTY
            if score > best_score:
                best_score = score
                best_move = cell

        return best_move

    def minimax(
        self,
        board: Board,
        cell: BoardCell,
        depth: int,
        is_maximizing: bool,
        alpha: int,
        beta: int,
        state: BoardCellState,
    ) -> int:
        win_state_eval = board.evaluate_win(cell=cell, state=state)
        if win_state_eval is not WinState.DRAW:
            return win_state_eval.value
        elif len(list(board.get_empty_cells())) == 0 or depth == 0:
            return WinState.DRAW.value

        next_state = (
            BoardCellState.AI
            if state is BoardCellState.PLAYER
            else BoardCellState.PLAYER
        )

        for cell in board.get_empty_cells():
            cell.state = next_state
            score = self.minimax(
                board=board,
                cell=cell,
                depth=depth - 1,
                is_maximizing=not is_maximizing,
                alpha=alpha,
                beta=beta,
                state=next_state,
            )
            if is_maximizing:
                alpha = max(score, alpha)
            else:
                beta = min(score, beta)
            cell.state = BoardCellState.EMPTY
            if alpha >= beta:
                break

        if is_maximizing:
            return alpha
        else:
            return beta

    def make_move(self, board: Board) -> None:
        chance = random.choice([0, 1])
        if chance == 0:
            cell_move = board.get_random_empty()
        else:
            cell_move = self.find_best_move(board)

        if cell_move is not None:
            cell_move.state = BoardCellState.AI

            self.win = (
                board.evaluate_win(cell=cell_move, state=BoardCellState.AI)
                is WinState.AI
            )
