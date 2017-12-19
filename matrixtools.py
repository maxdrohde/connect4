from helpers import colors, shapes
import copy
from operator import itemgetter
import random

height = 6
width = 7

blank = colors.WHITE + shapes.CIRCLE + colors.ENDC
color1 = colors.CYAN + shapes.CIRCLE + colors.ENDC
color2 = colors.RED + shapes.CIRCLE + colors.ENDC

row = [blank for x in range(width)]
board = [row[:] for x in range(height)]

def best_column(board,color):
    open_columns = available_columns(board)
    column_point_array = []

    for column in open_columns:
        new_board = drop(board,column,color)
        column_point_array.append((column,eval_board(new_board,color)))

    highest_val = max(column_point_array,key=itemgetter(1))[1]

    rand_choices = []
    for item in column_point_array:
        if item[1]== highest_val:
            rand_choices.append(item[0])

    best = random.choice(rand_choices)

    return((best,highest_val))

def worst_column(board,color):
    open_columns = available_columns(board)
    column_point_array = []

    for column in open_columns:
        new_board = drop(board,column,color)
        column_point_array.append((column,eval_enemy_board(new_board,color)))

    highest_val = max(column_point_array,key=itemgetter(1))[1]


    rand_choices = []
    for item in column_point_array:
        if item[1]== highest_val:
            rand_choices.append(item[0])

    best = random.choice(rand_choices)

    return((best,highest_val))

def create_board():
    row = [blank for x in range(width)]
    board = [row[:] for x in range(height)]
    return(board)

def print_board(array):
    column_numbers = '  ' + ' '.join([str(i+1) for i in range(width)])
    print(column_numbers)
    print(shapes.BAR_TOP_LEFT + shapes.BAR_H *width * 2 + shapes.BAR_TOP_RIGHT)

    for row in array:
        row_str = ' '.join(row)
        print(shapes.BAR_V + row_str + " " + shapes.BAR_V)

    print(shapes.BAR_BOTTOM_LEFT + shapes.BAR_H * width * 2 + shapes.BAR_BOTTOM_RIGHT)


def check_win(array, color):
# takes in an array and a color - if that color winning, return True
    inarow = 4
    win = (x_in_a_row(array, color, inarow) or
           x_in_a_row(transpose(array), color, inarow) or
           x_in_a_row(get_diagonals(array),color, inarow))

    return(win)


def drop(array, column_number, color):
# takes in a column and a color and returns the game board after that move

    board = copy.deepcopy(array)

    column_number = column_number - 1
    column = []
    for row in array:
        column.append(row[column_number])

    current_row = len(column)-1
    while (column[current_row]!=blank):
        current_row = current_row -1
        if current_row == -1:
            print('\007')
            return(False)

    board[current_row][column_number] = color
    return(board)

def get_diagonals(board,flipped = False):
    """
    takes in board, returns diagnols

    Generally, this function should not be called with flipped = True,
    which will only return diagonals in this direction: /
    """
    brd = [x[::-1] for x in board] if flipped else board[:]
    diag_down = []

    # Get diagonals from bottom left to the middle
    for row in range(height - 1, -1, -1):
        diag_length = min(height, height - row)
        diag = ''.join([brd[row + i][i] for i in range(diag_length)])
        diag_down.append(diag)

    # Get diagonals from one past the middle to the top right
    for col in range(1, width):
        diag_length = min(height, width - col)
        diag = ''.join([brd[i][col + i] for i in range(diag_length)])
        diag_down.append(diag)

    # Get diagonals in the other direction by calling recursively with the
    # board flipped
    if not flipped:
        d = get_diagonals(board,flipped = True)
        diag_down += d

    return(diag_down)

def x_in_a_row(array,color,x):
    for row in array:
        row_string = ''.join(row)
        if color*x in row_string:
            return(True)
    return(False)

def check_full(array):
    """Checks if the board has no more available moves"""
    for row in board:
        for piece in row:
            if piece == blank:
                return(False)
    return(True)

def available_columns(array):
    # takes in an array and returns the open columns in a list
    available_columns = []
    for column in range(0,7):
        if array[0][column] == blank:
            available_columns.append(column+1)
    return(available_columns)

def transpose(array):
    return ([list(x) for x in zip(*array)])

def eval_board(array,color):
    points_array = []

    if x_in_a_row(array,color,3):
        points_array.append(100)
    if x_in_a_row(array,color,4):
        points_array.append(150000)


    if x_in_a_row(transpose(array),color,3):
        points_array.append(100)
    if x_in_a_row(transpose(array),color,4):
        points_array.append(150000)

    if x_in_a_row(get_diagonals(array),color,3):
        points_array.append(100)
    if x_in_a_row(get_diagonals(array),color,4):
        points_array.append(150000)

    return(sum(points_array))

def eval_enemy_board(array,color):
    points_array = []
    if x_in_a_row(array,color,4):
        points_array.append(100000)

    if x_in_a_row(transpose(array),color,4):
        points_array.append(100000)

    if x_in_a_row(get_diagonals(array),color,4):
        points_array.append(100000)

    if x_in_a_row(array,color,3):
        points_array.append(1000)

    if x_in_a_row(transpose(array),color,3):
        points_array.append(1000)

    if x_in_a_row(get_diagonals(array),color,3):
        points_array.append(1000)

    return(sum(points_array))
