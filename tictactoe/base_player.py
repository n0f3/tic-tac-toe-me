from .board import Board


class BasePlayer:
    win = False
    opponent = None

    def make_move(self, board: Board) -> None:
        raise NotImplementedError
