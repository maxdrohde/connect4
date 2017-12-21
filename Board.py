from helpers import colors, shapes

class Board:

    def __init__(self, c1, c2):
        self.height = 6
        self.width = 7
        self.blank = colors.WHITE + shapes.CIRCLE + colors.ENDC

        self.color1 = c1
        self.color2 = c2

        row = [self.blank for x in range(self.width)]
        self.board = [row[:] for x in range(self.height)]


    def drop(self, column_number, player_color):
        column_number = column_number - 1
        column = []
        for row in self.board:
            column.append(row[column_number])

        current_row = len(column)-1
        while (column[current_row]!=self.blank):
            current_row = current_row -1
            if current_row == -1:
                print('\007')
                return(False)

        piece = player_color

        self.board[current_row][column_number] = piece
        return(True)

    def get_diagonals(self, flipped = False):
        """Recursively finds all diagonals in the current board

        Generally, this function should not be called with flipped = True,
        which will only return diagonals in this direction: /
        """
        brd = [x[::-1] for x in self.board] if flipped else self.board[:]
        diag_down = []

        # Get diagonals from bottom left to the middle
        for row in range(self.height - 1, -1, -1):
            diag_length = min(self.height, self.height - row)
            diag = [brd[row + i][i] for i in range(diag_length)]
            diag_down.append(diag)

        # Get diagonals from one past the middle to the top right
        for col in range(1, self.width):
            diag_length = min(self.height, self.width - col)
            diag = [brd[i][col + i] for i in range(diag_length)]
            diag_down.append(diag)

        # Get diagonals in the other direction by calling recursively with the
        # board flipped
        if not flipped:
            d = self.get_diagonals(flipped = True)
            diag_down += d

        return(diag_down)

    def x_in_a_row(self,array,x):
        """Given a list of lists or strings, returns whether there are x
           non-blank elements in a row in any of the lists or strings.
        """
        for row in array:
            unique = set(row)
            if self.blank in unique:
                unique.remove(self.blank)
            if not unique:
                continue

            row_string = ''.join(row)
            for color in iter(unique):
                if color * x in row_string:
                    return(True)
        return(False)

    def check_full(self):
        """Checks if the board has no more available moves"""
        for row in self.board:
            for piece in row:
                if piece == self.blank:
                    return(False)
        return(True)

    def transpose(self,array):
        return ([list(x) for x in zip(*array)])

    def print_board(self):
        column_numbers = '  ' + ' '.join([str(i+1) for i in range(self.width)])
        print(column_numbers)
        print(shapes.BAR_TOP_LEFT + shapes.BAR_H * self.width * 2 + shapes.BAR_TOP_RIGHT)

        for row in self.board:
            row_str = ' '.join(row)
            print(shapes.BAR_V + row_str + " " + shapes.BAR_V)

        print(shapes.BAR_BOTTOM_LEFT + shapes.BAR_H * self.width * 2 + shapes.BAR_BOTTOM_RIGHT)

    def check_win(self):
        """Determines if the board is in a game over state

        If a player has won the game, return True.
        If the board is full and nobody has won, return "tie".
        Otherwise, return False
        """
        inarow = 4
        win = (self.x_in_a_row(self.board, inarow) or
               self.x_in_a_row(self.transpose(self.board), inarow) or
               self.x_in_a_row(self.get_diagonals(), inarow))

        if not win and self.check_full():
            win = "tie"

        return(win)
