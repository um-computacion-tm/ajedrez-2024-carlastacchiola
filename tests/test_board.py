from main.board import Board
import unittest


class TestBoard(unittest.TestCase):
    def test_create_board(self):
        board = Board()
        self.assertNotEqual(board, None)


if __name__ == "__main__":
    unittest.main()