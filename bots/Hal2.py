import helpers as hlp
import random

class Hal2:
    def __init__(self):
        self.name = "Hal2"
        self.player_color = None
        self.red = None
        self.blue = None

    def other(self,color,blue,red):
        if color == red:
            return(blue)
        else:
            return(red)


    def num_in_column(self,board,column_number,color):
    # inputs a column number and a player number, and returns the number of pieces the player has in that column
        tboard = hlp.transpose(board)
        column = tboard[column_number]

        count = []
        for item in column:
            if item == color:
                count.append(item)
        return(len(count))

    def play_piece(self, board):
        self.red = board.red
        self.blue = board.blue

        pieces_per_column = [self.num_in_column(board.board,num,self.other(self.player_color,self.blue,self.red)) for num in range(0,7)]
        best = max([(v,i) for i,v in enumerate(pieces_per_column)])[1]
        if board.board[0][best] == board.blank:
            return(best+1)
        else:
            while board.board[0][best] != board.blank:
                best = random.randint(0,6)
            return(best+1)
