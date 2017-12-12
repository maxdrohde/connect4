from random import randint

class R2D2:
    def __init__(self):
        self.name = "R2D2"
        self.player_color = None
        self.red = None
        self.blue = None

    def play_piece(self, board):
        # Find a new column if the randomly chosen one is full
        rand_col = self.get_random_column()
        while board.board[0][rand_col] != board.blank:
            rand_col = self.get_random_column()

        # The board columns are numbered for humans, so increase by one
        return (rand_col+1)

    def get_random_column(self):
        rand_num = randint(0, 6)
        return(rand_num)
