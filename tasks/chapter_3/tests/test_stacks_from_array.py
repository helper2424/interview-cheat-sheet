from unittest import TestCase
from stacks_from_array import Stack

class TestChechPalindrom(TestCase):
    def test_push_1_element(self):
        stack = Stack()
        stack.push(0, 1)
        self.assertEqual([1, None, None, None, None, None, None, None, None], stack.internal)

        stack.push(1, 2)
        self.assertEqual([1, None, None, 2, None, None, None, None, None], stack.internal)

        stack.push(2, 3)
        self.assertEqual([1, None, None, 2, None, None, 3, None, None], stack.internal)

    def test_push_til_full_stack(self):
        stack = Stack()
        stack.push(1, 100)
        for i in range(1, 15):
            stack.push(0, i)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 13, 14, 100, None, None, None, None, None], stack.internal)
