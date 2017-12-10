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
    number = input('Column?     ')
    while not number.isdigit() or int(number) not in range(1,8):
        number = input('Enter a proper column number!')

    return(int(number))

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
