
class Board: 
    def __init__(self): 
        self.__positions__ = []
        for _ in range(8): 
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
 
    def get_piece(self, row, col):
        return self.__positions__[row] [col]
    
    