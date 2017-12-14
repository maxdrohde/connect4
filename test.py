import helpers as hlp

height = 6
width = 7

row = [x for x in range(width)]
board = [row[:] for x in range(height)]
board[5][3] = 6
tboard = hlp.transpose(board)

tboard


for column in tboard:
    success = []
    for item in column:
        if item == 0:
            box.append(item)
    print(len(success))



my_list = [5,4,7,5,90,6]
max([(v,i) for i,v in enumerate(my_list)])
