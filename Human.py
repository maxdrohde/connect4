class Human:
    def __init__(self, name, color):
        self.name = name
        self.player_color = color

    def play_piece(self, board):
        number = input('Column?     ')
        ok_columns = range(1, board.width + 1)

        while not number.isdigit() or int(number) not in ok_columns:
            number = input('Enter a proper column number!')

        return(int(number))
