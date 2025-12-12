from Board import Board
class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board: "Board"):
        raise NotImplementedError
from player import Player

class HumanPlayer(Player):
    def get_move(self, board):
        while True:
            try:
                r = int(input("Enter row (0-2): "))
                c = int(input("Enter col (0-2): "))
                if 0 <= r <= 2 and 0 <= c <= 2:
                    return r, c
            except:
                pass
            print("Invalid move. Try again.")
