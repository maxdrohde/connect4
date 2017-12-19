from helpers import colors, shapes
from matrixtools import *


class MATRIX:
    def __init__(self, color):
        self.name = "MATRIX"
        self.player_color = color
        self.enemy_color = None

    def play_piece(self, board):
        if not self.enemy_color:
            if board.color1 == self.player_color: self.enemy_color = board.color2
            if board.color2 == self.player_color: self.enemy_color = board.color1 

        array = board.board
        my_row = best_column(array,self.player_color)
        enemy_row = worst_column(array,self.enemy_color)

        if enemy_row[1] > my_row[1]:
            #print(enemy_row[0],enemy_row[1])
            return(enemy_row[0])
        else:
            #print(my_row[0],my_row[1])
            return(my_row[0])
