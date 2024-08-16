class Chess: 
    def __init__(self, board):
        self.__board__ = board()
        self.__turn__ = "WHITE"

    def move(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        ...
        
def change_turn(self):
    if self.turn == 'WHITE': 
        self.turn = 'BLACK'
    else:
        self.turn = 'WHITE'

