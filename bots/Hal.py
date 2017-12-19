class Hal:
    def __init__(self, color):
        self.name = "Hal"
        self.player_color = color

    def play_piece(self, board):
        """ Always chooses the furthest left column """
        col = 0

        # Find first column that has room to drop a piece
        while board.board[0][col] != board.blank:
            col += 1

        # The board columns are numbecolor2 for humans, so increase by one
        return col + 1
