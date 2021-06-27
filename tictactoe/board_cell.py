from enum import Enum, auto


class BoardCellState(Enum):
    EMPTY = auto()
    PLAYER = auto()
    AI = auto()


class BoardCell:
    state = BoardCellState.EMPTY
    position = (-1, -1)

    def __str__(self) -> str:
        if self.state is BoardCellState.EMPTY:
            return " "
        elif self.state is BoardCellState.PLAYER:
            return self.player_symbol
        else:
            return self.ai_symbol

    def __init__(
        self, position: (int, int), player_symbol: str, ai_symbol: str
    ) -> None:
        self.position = position
        self.player_symbol = player_symbol
        self.ai_symbol = ai_symbol
