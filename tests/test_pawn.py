import unittest
from main.pawn import Pawn

class TestPawn(unittest.TestCase):

    def test_black_pawn_symbol(self):
        black_pawn = Pawn("BLACK")
        self.assertEqual(str(black_pawn), "♟")

    def test_white_pawn_symbol(self):
        white_pawn = Pawn("WHITE")
        self.assertEqual(str(white_pawn), "♙")


if __name__ == '__main__':
    unittest.main()
