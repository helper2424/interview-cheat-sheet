from unittest import TestCase
from sum_numbers import sum as f, sum_forward_order as f2
from node import Node

def convert_list_to_array(list):
    root = list
    result = []
    while(root != None):
        result.append(root.value)
        root = root.next

    return result


def convert_array_to_list(array):
    root = Node(array[0])
    for i in range(1, len(array)):
        root.add_node(array[i])

    return root

class TestSumNumbers(TestCase):
    def test_sum(self):
        a = convert_array_to_list([7, 1, 6])
        b = convert_array_to_list([5, 9, 2])
        self.assertEqual([2, 1, 9], convert_list_to_array(f(a, b)))

        a = convert_array_to_list([7])
        b = convert_array_to_list([5, 9, 2])
        self.assertEqual([2, 0, 3], convert_list_to_array(f(a, b)))

        a = convert_array_to_list([7])
        b = convert_array_to_list([9])
        self.assertEqual([6, 1], convert_list_to_array(f(a, b)))

        a = convert_array_to_list([7])
        self.assertEqual([7], convert_list_to_array(f(None, a)))

        a = convert_array_to_list([7])
        self.assertEqual([7], convert_list_to_array(f(a, None)))
        self.assertEqual([], convert_list_to_array(f(None, None)))

    def test_sum_forward_order(self):
        a = convert_array_to_list([6, 1, 7])
        b = convert_array_to_list([2, 9, 5])
        self.assertEqual([9, 1, 2], convert_list_to_array(f2(a, b)))

        a = convert_array_to_list([7])
        b = convert_array_to_list([2, 9, 5])
        self.assertEqual([3, 0, 2], convert_list_to_array(f2(a, b)))

        a = convert_array_to_list([7])
        b = convert_array_to_list([9])
        self.assertEqual([1 ,6], convert_list_to_array(f2(a, b)))

        a = convert_array_to_list([7])
        self.assertEqual([7], convert_list_to_array(f2(None, a)))

        a = convert_array_to_list([7])
        self.assertEqual([7], convert_list_to_array(f2(a, None)))
        self.assertEqual([], convert_list_to_array(f2(None, None)))
