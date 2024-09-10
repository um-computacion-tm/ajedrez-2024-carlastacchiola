from main.board import Board
from main.chess import Chess
import unittest


class TestChess(unittest.TestCase):
    def test_initial_turn(self):
        chess = Chess()
        board = Board()
        self.assertEqual(self.game.turn, "WHITE")


if __name__ == "__main__":
    unittest.main()
