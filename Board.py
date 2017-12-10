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
        if self.check_row(self.board) or self.check_row(self.transpose(self.board)):
            return(True)
        else:
            return(False)
