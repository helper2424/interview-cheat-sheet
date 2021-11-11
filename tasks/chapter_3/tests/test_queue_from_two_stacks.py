from unittest import TestCase
from queue_from_two_stacks import Queue2Stacks

def add_n_items_to_queue(n, queue):
    for i in range(n):
        queue.append(i)

class TestQueue2Stacks(TestCase):
    def test_to_array(self):
        queue = Queue2Stacks()

        self.assertEqual([], queue.to_array())

        queue.push_stack = []
        queue.pop_stack = [3, 2, 1]
        self.assertEqual([3, 2, 1], queue.to_array())

        queue.push_stack = [1, 2, 3]
        queue.pop_stack = []
        self.assertEqual([3, 2, 1], queue.to_array())

        queue.push_stack = [4, 5, 6]
        queue.pop_stack = [3, 2, 1]
        self.assertEqual([6, 5, 4, 3, 2, 1], queue.to_array())


    def test_push(self):
        queue = Queue2Stacks()

        queue.push(1)
        self.assertEqual([1], queue.to_array())

        queue.push(2)
        self.assertEqual([2, 1], queue.to_array())

        queue.push(3)
        self.assertEqual([3, 2, 1], queue.to_array())

    def test_pop(self):
        queue = Queue2Stacks()

        queue.push(1)
        queue.push(2)
        queue.push(3)

        self.assertEqual([3, 2, 1], queue.to_array())

        self.assertEqual(1, queue.pop())
        self.assertEqual([3, 2], queue.to_array())

        self.assertEqual(2, queue.pop())
        self.assertEqual([3], queue.to_array())

        self.assertEqual(3, queue.pop())
        self.assertEqual([], queue.to_array())

        self.assertEqual(None, queue.pop())
        self.assertEqual([], queue.to_array())


    def test_peek(self):
        queue = Queue2Stacks()

        self.assertEqual(None, queue.peek())

        queue.push(1)
        self.assertEqual(1, queue.peek())

        queue.push(2)
        self.assertEqual(1, queue.peek())

        queue.push(3)
        queue.pop()

        self.assertEqual(2, queue.peek())