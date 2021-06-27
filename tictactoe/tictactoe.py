from .ai_player import AIPlayer
from .human_player import HumanPlayer
from .board import Board


def clear_output() -> None:
    print("\n" * 20)


class TicTacToe:
    def __init__(self) -> None:
        self.board = None
        self.win = False
        self.current_player = None
        self.player = None
        self.ai = None

    def __str__(self) -> str:
        return str(self.board)

    def reset_game(self) -> None:
        self.board.reset()
        self.win = False
        self.current_player = self.player

    def ask_user_symbol(self) -> None:
        player_symbol = ""
        while player_symbol not in ["X", "O"]:
            player_symbol = input("Choose which symbol you'll be (X) or (O)")
            player_symbol = player_symbol.upper()
        ai_symbol = "O" if player_symbol == "X" else "X"
        self.board = Board(player_symbol=player_symbol, ai_symbol=ai_symbol)
        self.player = HumanPlayer()
        self.ai = AIPlayer()

        self.player.opponent = self.ai
        self.ai.opponent = self.player
        self.current_player = self.player

    def play(self) -> None:
        if not self.board.moves_left():
            print("Draw!")
            self.reset_game()
            return

        self.current_player.make_move(board=self.board)

        print("\n" * 5)
        if self.current_player.win:
            print(self)
            if isinstance(self.current_player, HumanPlayer):
                print("Congratulations, you win!")
            else:
                print("Oh no, the computer won!")
            self.reset_game()
            return
        else:
            self.current_player = self.current_player.opponent
