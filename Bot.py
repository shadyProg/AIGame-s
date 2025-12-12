from player import Player
from minimax import MinimaxAI

class BotPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
        self.ai = MinimaxAI()

    def get_move(self, board):
        r, c = self.ai.find_best_move(board)
        print(f"Bot plays at: {r}, {c}")
        return r, c
