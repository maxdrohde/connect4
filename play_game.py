from Board import Board
from helpers import load_bot
import os, sys
import time
import copy


class Game:
    def __init__(self, bot1 = None, bot2 = None):
        self.game_board = Board()
        self.current_turn = 1
        self.bot1 = bot1
        self.bot2 = bot2

        if bot1:
            bot1.player_number = 1
        if bot2:
            bot2.player_number = 2

    def play(self):
        game_over = False

        while not game_over:
            os.system('clear')
            self.game_board.print_board()
            num = self.get_column()
            success = self.game_board.drop(num,self.current_turn)
            if success == True:
                if self.current_turn == 1:
                    self.current_turn = 2
                else:
                    self.current_turn = 1

            game_over = self.game_board.check_win()

        os.system('clear')
        self.game_board.print_board()

        if game_over == "tie":
            print("It's a tie!")
        else:
            print('Player '+str(self.flip(self.current_turn))+' wins!')

    def flip(self, x):
        if x == 1:
            return (2)
        else:
            return(1)

    def get_column(self):
        if self.current_turn == 1 and self.bot1 != None:
            number = self.bot1.play_piece(copy.deepcopy(self.game_board))
            time.sleep(0.5)
        elif self.current_turn == 2 and self.bot2 != None:
            number = self.bot2.play_piece(copy.deepcopy(self.game_board))
            time.sleep(0.5)
        else:
            number = input('Column?     ')
            while not number.isdigit() or int(number) not in range(1,8):
                number = input('Enter a proper column number!')
            number = int(number)

        return(number)

if __name__ == '__main__':
    bot1, bot2 = None, None
    if len(sys.argv) > 1:
        bot1 = load_bot(sys.argv[1])
    if len(sys.argv) > 2:
        bot2 = load_bot(sys.argv[2])

    game = Game(bot1, bot2)
    game.play()
