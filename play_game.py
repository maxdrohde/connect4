from Board import Board
import os
board = Board()

turn = 1

def flip(x):
    if x == 1:
        return (2)
    else:
        return(1)

def get_column():
    number = int(input('Column?     '))
    while number not in [1,2,3,4,5,6,7]:
        number = int(input('Enter a proper column number!'))
    return(number)

while board.check_win() == False:
    os.system('clear')
    board.print_board()
    num = get_column()
    success = board.drop(num,turn)
    if success == True:
        if turn == 1:
            turn = 2
        else:
            turn = 1

os.system('clear')
board.print_board()
print('Player '+str(flip(turn))+' wins!')
