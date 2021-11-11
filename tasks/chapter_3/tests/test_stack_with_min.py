from unittest import TestCase
from stack_with_min import StackWithMin

class TestStackWithMin(TestCase):
    def test_stack(self):
        stack = StackWithMin()
        stack.push(1)
        self.assertEqual(stack.min(), 1)

        stack.push(2)
        self.assertEqual(stack.min(), 1)

        stack.push(0)
        self.assertEqual(stack.min(), 0)

        stack.push(4)
        self.assertEqual(stack.min(), 0)

        stack.pop()
        self.assertEqual(stack.min(), 0)

        stack.pop()
        self.assertEqual(stack.min(), 1)

        stack.push(-1)
        self.assertEqual(stack.min(), -1)

        stack.pop()
        self.assertEqual(stack.min(), 1)
