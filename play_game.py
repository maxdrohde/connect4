from Board import Board
from Human import Human
import helpers
import os, sys
import time
import copy
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np

class Game:
    def __init__(self, p1 = None, p2 = None, sleep = 0.0, clear = True, display = True):
        self.player1 = p1
        self.player2 = p2
        self.game_board = Board(p1.player_color, p2.player_color)

        self.sleep_time = sleep # Controls the delay for the bots actions
        self.clear = clear # For debugging - prints all the boards if false
        self.display = display # If running simulations - keep false

        # The current turn keeps track of the color of the current player
        self.current_turn = self.player1.player_color

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

            if success != False and not game_over:
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
            #print("It's a tie!")
            return('Tie')
        else:
            winner = self.color_to_bot(self.current_turn) # current_turn is color

            if self.display == True:
                print(winner+' wins!')

            return(winner)

    def switch_turns(self):
        if self.current_turn == self.player1.player_color:
            self.current_turn = self.player2.player_color
        else:
            self.current_turn = self.player1.player_color

    def color_to_bot(self, color):
        """Takes in a color and returns bot"""
        if self.player1 and color == self.player1.player_color:
            return(self.player1.name)
        elif self.player2 and color == self.player2.player_color:
            return(self.player2.name)
        else:
            return("Human")

    def get_column(self):
        """Request a column number from the current player"""
        if self.player1 != None and self.player1.player_color == self.current_turn:
            number = self.player1.play_piece(copy.deepcopy(self.game_board))
            time.sleep(self.sleep_time)
        elif self.player2 != None and self.player2.player_color == self.current_turn:
            number = self.player2.play_piece(copy.deepcopy(self.game_board))
            time.sleep(self.sleep_time)
        else:
            # Ask a human
            number = input('Column?     ')
            while not number.isdigit() or int(number) not in range(1, self.game_board.width + 1):
                number = input('Enter a proper column number!')
            number = int(number)

        return(number)


class Tournament:
    def __init__(self, p1, p2, num_games, track = False, plot = False, game_opts = []):
        self.player1 = p1
        self.player2 = p2
        self.num_games = num_games
        self.tracking = track
        self.winners = []

        if self.player1.name == self.player2.name:
            self.player1.name = self.player1.name + "_1"
            self.player2.name = self.player2.name + "_2"

    def start(self):
        start_time = time.time()

        for i in range(self.num_games):
            if i % 2 == 0:
                game = Game(self.player1, self.player2)
            else:
                game = Game(self.player2, self.player1)
            self.winners.append(game.play())
            if self.tracking: print(i)

        time_elapsed = time.time() - start_time
        self.display_results(time_elapsed)

    def display_results(self, elapsed):
        b1_wins = str(self.winners.count(self.player1.name))
        b2_wins = str(self.winners.count(self.player2.name))
        ties = str(self.winners.count('Tie'))

        print('------------RESULTS-------------')
        print(self.player1.name + ' won ' + b1_wins + ' times')
        print(self.player2.name + ' won ' + b2_wins + ' times')
        print('There were ' + ties + ' ties')

        print('--------------------------------')
        if ties != self.num_games:
            b1_win_rate = (int(b1_wins) / (int(b1_wins) + int(b2_wins))) * 100
            b2_win_rate = (int(b2_wins) / (int(b1_wins) + int(b2_wins))) * 100
        print(self.player1.name + ' win rate is ' + ("%.2f" % b1_win_rate) + ' %')
        print(self.player2.name + ' win rate is ' + ("%.2f" % b2_win_rate) + ' %')
        print('--------------------------------')

        print('This simulation took ' + ("%.2f" % elapsed) + ' seconds')
        print('--------------------------------')

        plot = False
        if plot == True:
        #Plots the wins for each bot
            x = np.arange(2)
            wins = [int(b1_wins), int(b2_wins)]
            fig, ax = plt.subplots()
            #plt.bar(x, wins,width=0.01)
            #plt.xticks(x, (self.player1.name, self.player2.name))
            ax = sns.barplot(x =[self.player1, self.player2.name], y = wins)
            plt.show()


if __name__ == '__main__':
    # Get command line arguments
    args = helpers.get_args()

    # Get pieces for the players
    color1 = helpers.colors.CYAN + helpers.shapes.CIRCLE + helpers.colors.ENDC
    color2 = helpers.colors.RED + helpers.shapes.CIRCLE + helpers.colors.ENDC

    # Load first bot if it exists
    if args.bot1 and args.bot2:
        player1 = helpers.load_bot(args.bot1, color1)
        player2 = helpers.load_bot(args.bot2, color2)
    elif args.bot1:
        human = Human(input("Player 1, enter your name: "), color1)
        bot = helpers.load_bot(args.bot1, color2)
        player1 = bot if args.g == 'bvh' else human
        player2 = human if player1 == bot else bot
    elif args.g == 'hvh' or args.g == None:
        player1 = Human(input("Player 1, enter your name: "), color1)
        player2 = Human(input("Player 2, enter your name: "), color2)
    else:
        print("Invalid options. Type play_game.py -h for help.")

    # If multiple rounds are specified, start a tournament
    if args.rounds > 1:
        t = Tournament(player1, player2, args.rounds)
        t.start()
    else:
        game = Game(player1, player2)
        winner = game.play()
