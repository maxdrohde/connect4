class Hal:
    def __init__(self):
        self.name = "Hal"

    def play_piece(self, board):
        """ Always chooses the furthest left column """
        col = 0
        row = 0

        # Find first column that has room to drop a piece
        while board.board[row][col] != board.blank:
            col += 1

        # The board columns are numbered for humans, so increase by one
        return col + 1
