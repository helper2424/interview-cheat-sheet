from unittest import TestCase
from cheat_matrix import cheat_matrix as f

class TestReverseString(TestCase):
    def test_reverse_string(self):
        self.assertEqual([[]], f([[]]))
        self.assertEqual([[1]], f([[1]]))
        self.assertEqual([[0]], f([[0]]))
        self.assertEqual([[0, 0],
                          [0, 3]], f([[0, 1],
                                      [2, 3]]))
        self.assertEqual([[2, 0, 4, 0, 6],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]], f([[2, 1, 4, 5, 6],
                                               [2, 3, 6, 0, 7],
                                               [2, 0, 6, 2, 7]]))