from random import randint

class R2D2:
    def __init__(self, color):
        self.name = "R2D2"
        self.player_color = color

    def play_piece(self, board):
        """ Always chooses a random column """

        # All columns start out available. For example, this may start as a list
        # [0, 1, 2, 3, 4, 5, 6]
        available_columns = [i for i in range(len(board.board[0]))]
        rand_col = self.get_random_column()

        # Find a new column if the randomly chosen one is full
        rand_col = self.get_random_column()
        while board.board[0][rand_col] != board.blank:
            rand_col = self.get_random_column()

        # The board columns are numbecolor2 for humans, so increase by one
        return rand_col + 1

    def get_random_column(self):
        rand_num = randint(0, 6)
        return(rand_num)

# Available column functionality broken  - need to fix!
