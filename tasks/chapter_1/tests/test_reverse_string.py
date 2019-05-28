from unittest import TestCase
from reverse_string import reverse as f

class TestReverseString(TestCase):
    def test_reverse_string(self):
        self.assertEqual(f(''), '')
        self.assertEqual(f('1'), '1')
        self.assertEqual(f('12'), '21')
        self.assertEqual(f('121'), '121')
        self.assertEqual(f('0000'), '0000')
        self.assertEqual(f('1234567890'), '0987654321')
