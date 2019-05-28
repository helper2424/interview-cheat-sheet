from unittest import TestCase
from rotate_matrix import rotate_matrix as f, rotate_matrix_efficient as f2

class TestRotate_matrix(TestCase):
    def test_rotate_matrix(self):
        self.assertEqual([[3, 1],
                          [4, 2]],f([[1, 2],
                                     [3, 4]]))
        self.assertEqual([[2, 4],
                          [1, 3]],f([[1, 2],
                                     [3, 4]], True))
        self.assertEqual([[1]],f([[1]], True))
        self.assertEqual([[1]], f([[1]]))
        self.assertEqual([[7, 4, 1],
                          [8, 5, 2],
                          [9, 6, 3]],f([[1, 2, 3],
                                     [4, 5, 6],
                                     [7, 8, 9]]))

    def test_rotate_matrix_efficient(self):
        self.assertEqual([[3, 1],
                          [4, 2]],f2([[1, 2],
                                     [3, 4]]))
        self.assertEqual([[2, 4],
                          [1, 3]],f2([[1, 2],
                                     [3, 4]], True))
        self.assertEqual([[1]],f2([[1]], True))
        self.assertEqual([[1]], f2([[1]]))
        self.assertEqual([[7, 4, 1],
                          [8, 5, 2],
                          [9, 6, 3]],f2([[1, 2, 3],
                                     [4, 5, 6],
                                     [7, 8, 9]]))