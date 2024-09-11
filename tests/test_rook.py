from main.rook import Rook  
import unittest


class TestRook(unittest.TestCase):
    def setUp(self):
        self.white_rook = Rook("WHITE")
        self.black_rook = Rook("BLACK")

    #def test_str_method(self):
        #self.assertEqual(str(self.white_rook), "♜")
        #self.assertEqual(str(self.black_rook), "♖")

    #def test_possible_moves(self):
        
        #moves = self.white_rook.get_possible_moves(0, 0)
        #expected_moves = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                          #(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        #self.assertEqual(sorted(moves), sorted(expected_moves))

if __name__ == "__main__":
    unittest.main()
