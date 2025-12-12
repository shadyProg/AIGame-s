from Board import Board
from player import HumanPlayer
from Bot import BotPlayer

class Game:
    def __init__(self):
        self.board = Board()
        self.human = HumanPlayer('X')
        self.bot = BotPlayer('O')

    def start(self):
        turn = "HUMAN"

        while True:
            self.board.print_board()

            if turn == "HUMAN":
                r, c = self.human.get_move(self.board)
                if not self.board.make_move(r, c, 'X'):
                    print("Cell taken, try again.")
                    continue

                if self.board.check_winner('X'):
                    self.board.print_board()
                    print("You win!")
                    break

                turn = "BOT"

            else:
                r, c = self.bot.get_move(self.board)
                self.board.make_move(r, c, 'O')

                if self.board.check_winner('O'):
                    self.board.print_board()
                    print("Bot wins!")
                    break

                turn = "HUMAN"

            if self.board.is_full():
                self.board.print_board()
                print("Draw!")
                break


if __name__ == "__main__":
    Game().start()
