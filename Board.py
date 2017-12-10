class Board:

    def __init__(self):
        self.height = 6
        self.width = 7
        self.board = [['0' for x in range(self.width)] for x in range(self.height)]

    def drop(self,column_number,player_number):
        column_number = column_number - 1
        column = []
        for row in self.board:
            column.append(row[column_number])

        current_row = len(column)-1
        while (column[current_row]!='0'):
            current_row = current_row -1
            if current_row == -1:
                print('\007')
                return(False)
        self.board[current_row][column_number] = str(player_number)
        return(True)



    def check_row(self,array):
        for row in array:
            row_string = ''.join(row)
            if '1'*4 in row_string or '2'*4 in row_string:
                return(True)
        return(False)

    def transpose(self,array):
        return ([list(x) for x in zip(*array)])

    def print_board(self):
        for row in self.board:
            print(row)

    def check_win(self):
        if self.check_row(self.board) or self.check_row(self.transpose(self.board)):
            return(True)
        else:
            return(False)
