import helpers as hlp
import random

class Hal2:
    def __init__(self, color):
        self.name = "Hal2"
        self.player_color = color
        self.color2 = None
        self.color1 = None

    def other(self,color,color1,color2):
        if color == color2:
            return(color1)
        else:
            return(color2)


    def num_in_column(self, board, column_number, color):
    # Inputs a column number and a player number, and returns the number of
    # pieces the player has in that column
        tboard = hlp.transpose(board)
        column = tboard[column_number]

        count = []
        for item in column:
            if item == color:
                count.append(item)
        return(len(count))

    def play_piece(self, board):
        self.color2 = board.color2
        self.color1 = board.color1

        pieces_per_column = [self.num_in_column(board.board,num,self.other(self.player_color,self.color1,self.color2)) for num in range(0,7)]
        best = max([(v,i) for i,v in enumerate(pieces_per_column)])[1]
        if board.board[0][best] == board.blank:
            return(best+1)
        else:
            while board.board[0][best] != board.blank:
                best = random.randint(0,6)
            return(best+1)
