from helpers import colors, shapes

class Board:

    def __init__(self):
        self.height = 6
        self.width = 7

        self.blank = colors.WHITE + shapes.CIRCLE + colors.ENDC
        self.p1 = colors.CYAN + shapes.CIRCLE + colors.ENDC
        self.p2 = colors.RED + shapes.CIRCLE + colors.ENDC

        row = [self.blank for x in range(self.width)]
        self.board = [row[:] for x in range(self.height)]


    def drop(self,column_number,player_number):
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
        piece = self.p1 if player_number == 1 else self.p2
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
            diag = ''.join([brd[row + i][i] for i in range(diag_length)])
            diag_down.append(diag)

        # Get diagonals from one past the middle to the top right
        for col in range(1, self.width):
            diag_length = min(self.height, self.width - col)
            diag = ''.join([brd[i][col + i] for i in range(diag_length)])
            diag_down.append(diag)

        # Get diagonals in the other direction by calling recursively with the
        # board flipped
        if not flipped:
            d = self.get_diagonals(flipped = True)
            diag_down += d

        return(diag_down)

    def check_row(self,array):
        for row in array:
            row_string = ''.join(row)
            if self.p1*4 in row_string or self.p2*4 in row_string:
                return(True)
        return(False)

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
        win = (self.check_row(self.board) or
               self.check_row(self.transpose(self.board)) or
               self.check_row(self.get_diagonals()))
        return(win)
