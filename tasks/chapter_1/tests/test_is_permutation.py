from unittest import TestCase
from check_permutation import is_permutation as f

class TestIsPermutation(TestCase):
    def test_is_permutationg(self):
        self.assertTrue(f('', ''))
        self.assertTrue(f('11', '11'))
        self.assertTrue(f('1a', '1a'))
        self.assertTrue(f('abc', 'bac'))
        self.assertTrue(f('11223', '32121'))
        self.assertFalse(f('1122', '32121'))
        self.assertFalse(f('', '32121'))
        self.assertTrue(f('!@#$%^&*()_+', ')$%^&*(_+!@#'))
