EMPTY = '-'

class Board:
    def __init__(self):
        self.grid = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]

    def print_board(self):
        for row in self.grid:
            print(" | ".join(row))
        print()

    def make_move(self, r, c, symbol):
        if self.grid[r][c] == EMPTY:
            self.grid[r][c] = symbol
            return True
        return False

    def undo_move(self, r, c):
        self.grid[r][c] = EMPTY

    def is_full(self):
        for row in self.grid:
            if EMPTY in row:
                return False
        return True

    def check_winner(self, symbol):
        # Rows
        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True
        
        # Columns
        for c in range(3):
            if (self.grid[0][c] == symbol and
                self.grid[1][c] == symbol and
                self.grid[2][c] == symbol):
                return True
        
        # Diagonals
        if (self.grid[0][0] == symbol and
            self.grid[1][1] == symbol and
            self.grid[2][2] == symbol):
            return True

        if (self.grid[0][2] == symbol and
            self.grid[1][1] == symbol and
            self.grid[2][0] == symbol):
            return True
        
        return False
