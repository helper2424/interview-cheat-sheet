from unittest import TestCase
from check_count_symbols_equal_one import check_count_symbols_equal_one as f
from check_count_symbols_equal_one import check_count_symbols_equal_one2 as f2

class TestCheckCOuntSymbolsEqualOne(TestCase):
    def test_check_empty_string(self):
        self.assertTrue(f(''))

    def test_check_one_symbol(self):
        self.assertTrue(f('1'))

    def test_check_two_symbol(self):
        self.assertFalse(f('11'))

    def test_true_negative_symbol(self):
        self.assertFalse(f('abcdegh!!'))


class TestCheckCOuntSymbolsEqualOne2(TestCase):
    def test_check_empty_string(self):
        self.assertTrue(f2(''))

    def test_check_one_symbol(self):
        self.assertTrue(f2('1'))

    def test_check_two_symbol(self):
        self.assertFalse(f2('11'))

    def test_true_negative_symbol(self):
        self.assertFalse(f2('abcdegh!!'))