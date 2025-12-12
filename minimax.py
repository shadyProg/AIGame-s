import math
from Board import EMPTY

AI = 'O'
HUMAN = 'X'

class MinimaxAI:
    def evaluate(self, board):
        if board.check_winner(AI):
            return +10
        if board.check_winner(HUMAN):
            return -10
        return 0

    def minimax(self, board, depth, isMax, alpha, beta):
        score = self.evaluate(board)

        if score == 10:
            return score - depth
        if score == -10:
            return score + depth
        if board.is_full():
            return 0

        if isMax:
            best = -math.inf
            for r in range(3):
                for c in range(3):
                    if board.grid[r][c] == EMPTY:
                        board.grid[r][c] = AI
                        value = self.minimax(board, depth + 1, False, alpha, beta)
                        board.grid[r][c] = EMPTY
                        best = max(best, value)
                        alpha = max(alpha, best)
                        if beta <= alpha:
                            return best
            return best

        else:
            best = math.inf
            for r in range(3):
                for c in range(3):
                    if board.grid[r][c] == EMPTY:
                        board.grid[r][c] = HUMAN
                        value = self.minimax(board, depth + 1, True, alpha, beta)
                        board.grid[r][c] = EMPTY
                        best = min(best, value)
                        beta = min(beta, best)
                        if beta <= alpha:
                            return best
            return best

    def find_best_move(self, board):
        best_value = -math.inf
        best_move = (-1, -1)

        for r in range(3):
            for c in range(3):
                if board.grid[r][c] == EMPTY:
                    board.grid[r][c] = AI
                    move_value = self.minimax(board, 0, False, -math.inf, math.inf)
                    board.grid[r][c] = EMPTY

                    if move_value > best_value:
                        best_value = move_value
                        best_move = (r, c)

        return best_move
