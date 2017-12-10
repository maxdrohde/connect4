from Board import Board
import os, sys

class Game:
    def __init__(self, bot1 = None, bot2 = None):
        self.game_board = Board()
        self.current_turn = 1

    def play(self):
        while self.game_board.check_win() == False:
            os.system('clear')
            self.game_board.print_board()
            num = self.get_column()
            success = self.game_board.drop(num,self.current_turn)
            if success == True:
                if self.current_turn == 1:
                    self.current_turn = 2
                else:
                    self.current_turn = 1

        os.system('clear')
        self.game_board.print_board()
        print('Player '+str(self.flip(self.current_turn))+' wins!')

    def flip(self, x):
        if x == 1:
            return (2)
        else:
            return(1)

    def get_column(self):
        number = input('Column?     ')
        while not number.isdigit() or int(number) not in range(1,8):
            number = input('Enter a proper column number!')

        return(int(number))

if __name__ == '__main__':
    game = Game()
    game.play()
