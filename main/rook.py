from .piece import Piece

class Rook(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        if self.__color__ == "BLACK":
            return "♖"
        
    def get_possible_moves(self, x, y):
        possible_moves = []

        for col in range(8):
            if not col == y:
                possible_moves.append((x, col))
        
        for row in range(8):
            if not row == x:
                possible_moves.append((row, y))

        return possible_moves
