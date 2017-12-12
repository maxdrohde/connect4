from random import randint

class R2D2:
    def __init__(self):
        self.name = "R2D2"
        self.player_number = None

    def play_piece(self, board):
        """ Always chooses a random column """

        # All columns start out available. For example, this may start as a list
        # [0, 1, 2, 3, 4, 5, 6]
        available_columns = [i for i in range(len(board.board[0]))]
        rand_col = self.get_random_column(available_columns)

        # Find a new column if the randomly chosen one is full
        while board.board[0][rand_col] != board.blank:
            available_columns.remove(rand_col)
            rand_col = self.get_random_column(available_columns)

        # The board columns are numbered for humans, so increase by one
        return rand_col + 1

    def get_random_column(self, available_columns):
        rand_num = randint(0, len(available_columns) - 1)
        return(available_columns[rand_num])
