from unittest import TestCase
from compress_string import compress_string as f

class TestCompress_string(TestCase):
    def test_compress_string(self):
        self.assertEqual(f(''), '')
        self.assertEqual(f('a'), 'a')
        self.assertEqual(f('aa'), 'aa')
        self.assertEqual(f('aaq'), 'aaq')
        self.assertEqual(f('abc'), 'abc')
        self.assertEqual(f('aaabbbc'), 'a3b3c1')
        self.assertEqual(f('111'), '13')
