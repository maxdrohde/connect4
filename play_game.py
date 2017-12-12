from Board import Board
from helpers import load_bot
import os, sys
import time
import copy
import matplotlib.pyplot as plt
import numpy as np


class Game:
    def __init__(self, bot1 = None, bot2 = None):
        self.game_board = Board()
        self.current_turn = 1
        self.bot1 = bot1
        self.bot2 = bot2
        self.sleep_time = 0.0 # Controls the delay for the bots actions
        self.clear = True # For debugging - prints all the boards if false
        self.display = False # If running simulations - keep false


        if bot1:
            bot1.player_color = self.game_board.blue
        if bot2:
            bot2.player_color = self.game_board.red

    def play(self):


        game_over = False

        while not game_over:

            if self.clear == True:
                os.system('clear')
            if self.display == True:
                self.game_board.print_board()
            num = self.get_column()
            success = self.game_board.drop(num,self.current_turn)
            if success == True:
                if self.current_turn == 1:
                    self.current_turn = 2
                else:
                    self.current_turn = 1

            game_over = self.game_board.check_win()

        if self.clear == True:
            os.system('clear')

        if self.display == True:
            self.game_board.print_board()

        if game_over == "tie":
            print("It's a tie!")
            return('Tie')
        else:
            num_winner = str(self.flip(self.current_turn))
            winner = self.number_to_bot(num_winner,self.bot1.name,self.bot2.name)

            if self.display == True:
                print(winner+' wins!')

            return(winner)

    def flip(self, x):
        if x == 1:
            return (2)
        else:
            return(1)

    def number_to_bot(self,number,b1,b2):
        if number == '1':
            return(b1)
        else:
            return(b2)

    def get_column(self):
        if self.current_turn == 1 and self.bot1 != None:
            number = self.bot1.play_piece(copy.deepcopy(self.game_board))
            time.sleep(self.sleep_time)
        elif self.current_turn == 2 and self.bot2 != None:
            number = self.bot2.play_piece(copy.deepcopy(self.game_board))
            time.sleep(self.sleep_time)
        else:
            number = input('Column?     ')
            while not number.isdigit() or int(number) not in range(1,8):
                number = input('Enter a proper column number!')
            number = int(number)

        return(number)

if __name__ == '__main__':
    bot1, bot2, rounds = None, None, 1
    if len(sys.argv) > 1:
        bot1 = load_bot(sys.argv[1])
    if len(sys.argv) > 2:
        bot2 = load_bot(sys.argv[2])
    if len(sys.argv) > 3:
        rounds = sys.argv[3]

    start = time.time()

    winners = []
    #This is the game loop
    for x in range(int(rounds)):
        game = Game(bot1, bot2)
        winners.append(game.play())

    end = time.time()
    elapsed = end - start

    b1_wins = str(len([x for x in winners if x == bot1.name]))
    b2_wins = str(len([x for x in winners if x == bot2.name]))
    ties = str(len([x for x in winners if x == 'Tie']))
    print(bot1.name + ' won '+b1_wins+ ' times')
    print(bot2.name + ' won '+b2_wins+ ' times')
    print('There were '+ties+' ties')
    print('This simulation took ' + str(elapsed) + ' seconds')

#Plots the wins for each bot
    x = np.arange(2)
    wins = [int(b1_wins),int(b2_wins)]
    fig, ax = plt.subplots()
    plt.bar(x, wins)
    plt.xticks(x, (bot1.name,bot2.name))
    plt.show()
