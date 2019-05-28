from unittest import TestCase
from replace_string import relace_space_to_20 as f

class TestReplace(TestCase):
    def test_is_permutationg(self):
        self.assertEqual(f(''), '')
        self.assertEqual(f(' '), '%20')
        self.assertEqual(f('  '), '%20%20')
        self.assertEqual(f('a b'), 'a%20b')
        self.assertEqual(f('   b  '), '%20%20%20b%20%20')
