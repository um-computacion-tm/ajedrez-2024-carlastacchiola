
from main.rook import Rook
from main.horse import Horse
from main.bishop import Bishop 
from main.pawn import Pawn
from main.queen import Queen
from main.king import King


class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        
        # Pawns 
        self.__positions__[1][0] = Pawn("♟")
        self.__positions__[1][1] = Pawn("♟") 
        self.__positions__[1][2] = Pawn("♟") 
        self.__positions__[1][3] = Pawn("♟") 
        self.__positions__[1][4] = Pawn("♟") 
        self.__positions__[1][5] = Pawn("♟") 
        self.__positions__[1][6] = Pawn("♟")
        self.__positions__[1][7] = Pawn("♟")    
        self.__positions__[6][0] = Pawn("♙")
        self.__positions__[6][1] = Pawn("♙")
        self.__positions__[6][2] = Pawn("♙")
        self.__positions__[6][3] = Pawn("♙")
        self.__positions__[6][4] = Pawn("♙")
        self.__positions__[6][5] = Pawn("♙")
        self.__positions__[6][6] = Pawn("♙")
        self.__positions__[6][7] = Pawn("♙")

        #Rooks
        self.__positions__[0][0] = Rook("♜") 
        self.__positions__[0][7] = Rook("♜") 
        self.__positions__[7][7] = Rook("♖") 
        self.__positions__[7][0] = Rook("♖") 

        # Horses 
        self.__positions__[0][1] = Horse('♞')
        self.__positions__[0][6] = Horse('♞')
        self.__positions__[7][1] = Horse('♘')
        self.__positions__[7][6] = Horse('♘')

        # Bishops
        self.__positions__[0][2] = Bishop('♝')
        self.__positions__[0][5] = Bishop('♝')
        self.__positions__[7][2] = Bishop('♗')
        self.__positions__[7][5] = Bishop('♗')

        # Queens
        self.__positions__[0][3] = Queen('♛')
        self.__positions__[7][3] = Queen('♕')

        # Kings
        self.__positions__[0][4] = King('♚')
        self.__positions__[7][4] = King('♔')
        
    
       
    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str

    def get_piece(self, row, col):
        return self.__positions__[row][col]
  

  