from pieces import Piece

class Rook(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        if self.__color__ == "BLACK":
            return "♖"