from tictactoe.tictactoe import TicTacToe

if __name__ == "__main__":
    app = TicTacToe()
    try:
        app.ask_user_symbol()
        while not app.win:
            print(app)
            app.play()
    except KeyboardInterrupt:
        pass
