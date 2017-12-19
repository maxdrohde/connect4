import sys

class Bernard:
    def __init__(self, color):
        self.name = "Bernard"
        self.player_color = color

        self.last_board_grid = []
        self.board_grid = []
        self.board_width = 0
        self.board_height = 0

        self.blank = ''

    def play_piece(self, board):
        # Special case if it's the first turn
        if (not board.board[board.height - 1].count(self.player_color) and
            not board.board[board.height - 2].count(self.player_color)):
            return(self.first_turn(board))

        self.update_board(board)

        # Detect if we can win or block a win this turn
        choice = self.winning_move()
        c = choice

        if not choice:
            last_col = self.get_last_move()
            if not last_col or board.board[0][last_col] != board.blank:
                last_col = board.board[0].index(board.blank)

            choice = last_col + 1

        # Before returning, always update our board state
        ok = board.drop(choice, self.player_color)
        if not ok:
            print("Something went wrong :(")
            exit(1)

        self.update_board(board)
        self.board_grid = board.board

        return(choice)

    def get_last_move(self):
        """Returns the column (index) of the previous player's move"""
        col_of_last_play = None

        # Search through every row for a difference from the last_board_grid
        for row in range(self.board_height):
            for col in range(self.board_width):
                if self.board_grid[row][col] != self.last_board_grid[row][col]:
                    col_of_last_play = col
                    break
            if col_of_last_play != None: break

        return(col_of_last_play)

    def first_turn(self, board):
        # Play in the middle of the board
        ncol = board.width
        center = (ncol // 2) + 1

        # Initialize the board variables
        self.board_grid = board.board[:]
        board.drop(center, self.player_color)
        self.update_board(board)

        self.blank = board.blank

        return(center)

    def test3color1blank(self, row):
        if row.count(self.blank) != 1:
            return False
        elif row.count(self.player_color) == 3:
            return True
        elif row.count(self.player_color) == 0:
            return True
        else:
            return False

    def search3(self, r, c):
        # Check right
        if c + 3 < self.board_width:
            row = [self.board_grid[r][c+0], self.board_grid[r][c+1],
                   self.board_grid[r][c+2], self.board_grid[r][c+3]]
            if self.test3color1blank(row):
                return(r, c + row.index(self.blank))

        # Check diagonal up left
        if c - 3 >= 0 and r - 3 >= 0:
            row = [self.board_grid[r-0][c-0], self.board_grid[r-1][c-1],
                   self.board_grid[r-2][c-2], self.board_grid[r-3][c-3]]
            if self.test3color1blank(row):
                b = row.index(self.blank)
                if r-b+1 == self.board_height or self.board_grid[r-b+1][c-b] != self.blank:
                    return((r-b, c-b))

        # Check diagonal up right
        if c + 3 < self.board_width and r - 3 >= 0:
            row = [self.board_grid[r-0][c+0], self.board_grid[r-1][c+1],
                   self.board_grid[r-2][c+2], self.board_grid[r-3][c+3]]
            if self.test3color1blank(row):
                b = row.index(self.blank)
                # input("r: " + str(r) + " c: " + str(c) + " b: " + str(b))
                if r-b+1 == self.board_height or self.board_grid[r-b+1][c+b] != self.blank:
                    return((r-b, c+b))

        # Check up
        if r - 3 >= 0:
            row = [self.board_grid[r-0][c], self.board_grid[r-1][c],
                   self.board_grid[r-2][c], self.board_grid[r-3][c]]
            if self.test3color1blank(row):
                return((r-3,c))

        return(None)

    def winning_move(self):
        # start with the lowest left piece
        for row in range(self.board_height):
            for col in range(self.board_width):
                win = self.search3(row, col)
                # input("found piece " + str(row) + "," + str(col) + " and win=" + str(win))
                if win:
                    return(win[1] + 1)

        return(None)

    def update_board(self, board):
        # input('assigning last_board:\n' + ''.join(self.board_grid[:][4]) + '\n' + ''.join(self.board_grid[:][5]))
        # Copy current board to previous board
        self.last_board_grid = self.board_grid[:]

        # Update current board variables
        # input('assigning board_grid:\n' + ''.join(board.board[4]) + '\n' + ''.join(board.board[5]))
        self.board_grid = board.board
        self.board_width = board.width
        self.board_height = board.height
