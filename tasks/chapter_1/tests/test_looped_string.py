from unittest import TestCase
from looped_string import is_loop as f

class TestReplace(TestCase):
    def test_is_permutationg(self):
        self.assertFalse(f('', ''))
        self.assertFalse(f('1', ''))
        self.assertFalse(f('123', '314'))
        self.assertFalse(f('1233', '314'))
        self.assertTrue(f('1233', '3312'))
        self.assertTrue(f('1233', '3312'))
        self.assertTrue(f('1111', '1111'))
        self.assertFalse(f('123456789', '567891234'))
