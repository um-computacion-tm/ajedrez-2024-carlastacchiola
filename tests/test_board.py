from main.board import Board
from main.rook import Rook
import unittest


class TestBoard(unittest.TestCase):
    def test_create_board_len8(self):
        board = Board()
        self.assertEqual(len(board.__positions__),8)

    def test_matrix_8x8(self):
        board = Board()
        for i in range(8):
            self.assertEqual(len(board.__positions__[i]),8)

    def test_get_piece_00(self):
        board = Board()
        piece=board.get_piece(0,0)
        self.assertIsInstance(piece,Rook)

if __name__ == "__main__":
    unittest.main()
