from unittest import TestCase
from build_relevant_list import build_relevant_list as f

class TestRotate_matrix(TestCase):
    def test_rotate_matrix(self):
        self.assertEqual("0", f("1 1\n0"))
