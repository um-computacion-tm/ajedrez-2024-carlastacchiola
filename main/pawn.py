from piece import Piece

class Pawn(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♙"
        if self.__color__ == "BLACK":
            return "♟"