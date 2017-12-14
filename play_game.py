from Board import Board
from helpers import load_bot
import os, sys
import time
import copy
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



class Game:
    def __init__(self, bot1 = None, bot2 = None):
        self.game_board = Board()
        self.current_turn = self.game_board.blue
        self.bot1 = bot1
        self.bot2 = bot2

        self.sleep_time = 0.0 # Controls the delay for the bots actions
        self.clear = False # For debugging - prints all the boards if false
        self.display = False # If running simulations - keep false

        if bot1:
            bot1.player_color = self.game_board.blue
            bot1.enemy_color = self.game_board.red
        if bot2:
            bot2.player_color = self.game_board.red
            bot2.enemy_color = self.game_board.blue

    def play(self):

        game_over = False
        drop_attempts = 0

        while not game_over:
            if self.clear == True:
                os.system('clear')
            if self.display == True:
                self.game_board.print_board()

            num = self.get_column()
            success = self.game_board.drop(num, self.current_turn)
            drop_attempts += 1

            game_over = self.game_board.check_win()

            if success == True and not game_over:
                self.switch_turns()
                drop_attempts = 0

            if drop_attempts > 2:
                q = input("Too many failed attempts! Enter 'q' to quit. ")
                if q == 'q': exit(1)

        # Game has ended!
        if self.clear == True:
            os.system('clear')

        if self.display == True:
            self.game_board.print_board()

        if game_over == "tie":
            print("It's a tie!")
            return('Tie')
        else:
            winner = self.color_to_bot(self.current_turn) # current_turn is color

            if self.display == True:
                print(winner+' wins!')

            return(winner)

    def switch_turns(self):
        if self.current_turn == self.game_board.red:
            self.current_turn = self.game_board.blue
        else:
            self.current_turn = self.game_board.red

    def color_to_bot(self, color):
        """Takes in a color and returns bot"""
        if self.bot1 and color == self.bot1.player_color:
            return(self.bot1.name)
        elif self.bot2 and color == self.bot2.player_color:
            return(self.bot2.name)
        else:
            return("Human")

    def get_column(self):
        """Request a column number from the current player"""
        if self.bot1 != None and self.bot1.player_color == self.current_turn:
            number = self.bot1.play_piece(copy.deepcopy(self.game_board))
            time.sleep(self.sleep_time)
        elif self.bot2 != None and self.bot2.player_color == self.current_turn:
            number = self.bot2.play_piece(copy.deepcopy(self.game_board))
            time.sleep(self.sleep_time)
        else:
            # Ask a human
            number = input('Column?     ')
            while not number.isdigit() or int(number) not in range(1, self.game_board.width + 1):
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
        try:
            rounds = int(sys.argv[3])
        except ValueError:
            print("Argument for number of rounds invalid")
            exit(1)

    start = time.time()

    winners = []
    #This is the game loop
    for x in range(int(rounds)):
        game = Game(bot1, bot2)
        winners.append(game.play())
        print(x)

    end = time.time()
    elapsed = end - start

    if rounds > 1:
        b1_wins = str(len([x for x in winners if x == bot1.name]))
        b2_wins = str(len([x for x in winners if x == bot2.name]))
        ties = str(len([x for x in winners if x == 'Tie']))
        print('------------RESULTS-------------')
        print(bot1.name + ' won '+b1_wins+ ' times')
        print(bot2.name + ' won '+b2_wins+ ' times')
        print('There were '+ties+' ties')

        print('--------------------------------')
        b1_win_rate = (int(b1_wins)/(int(b1_wins)+int(b2_wins)))*100
        b2_win_rate = (int(b2_wins)/(int(b1_wins)+int(b2_wins)))*100
        print(bot1.name + ' win rate is '+ ("%.2f" % b1_win_rate)+' %')
        print(bot2.name + ' win rate is '+ ("%.2f" % b2_win_rate)+' %')
        print('--------------------------------')

        print('This simulation took ' + ("%.2f" % elapsed) + ' seconds')
        print('--------------------------------')

        plot = False
        if plot == True:
        #Plots the wins for each bot
            x = np.arange(2)
            wins = [int(b1_wins),int(b2_wins)]
            fig, ax = plt.subplots()
            #plt.bar(x, wins,width=0.01)
            #plt.xticks(x, (bot1.name,bot2.name))
            ax = sns.barplot(x =[bot1.name,bot2.name], y = wins)
            plt.show()
