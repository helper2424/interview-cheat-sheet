from unittest import TestCase
from sort_stack import sort

class TestStackSort(TestCase):
    def test_empty(self):
        stack = []
        sort(stack)
        self.assertEqual([], stack)


    def test_order_items(self):
        stack = [1, 2, 3, 5]
        sort(stack)
        self.assertEqual([5, 3, 2, 1], stack)


    def test_random_array(self):
        stack = [10, 2, 4, 11, 8, -1, 0, 34, 34, 55, 55, 68, 90, 100, 55, 4, 11, 0]
        sort(stack)
        self.assertEqual([100, 90, 68, 55, 55, 55, 34, 34, 11, 11, 10, 8, 4, 4, 2, 0, 0, -1], stack)

