from unittest import TestCase
from list_partial_sorting import sort as f
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

class TestRemoveDuplicates(TestCase):
    def test_sort(self):
        self.assertEqual([1], convert_list_to_array(f(convert_array_to_list([1]), 10)))
        self.assertEqual([1], convert_list_to_array(f(convert_array_to_list([1]), 1)))
        self.assertEqual(None, f(None, 10))
        self.assertEqual([1, 2, 3], convert_list_to_array(f(convert_array_to_list([1, 2, 3]), 1)))
        self.assertEqual([1, 3, 2], convert_list_to_array(f(convert_array_to_list([3, 2, 1]), 2)))
        self.assertEqual([3, 3, 3, 3, 3], convert_list_to_array(f(convert_array_to_list([3, 3, 3, 3, 3]), 2)))
        self.assertEqual([3, 3, 3, 3, 3], convert_list_to_array(f(convert_array_to_list([3, 3, 3, 3, 3]), 3)))
        self.assertEqual([2, 9, 14, 78, 56], convert_list_to_array(f(convert_array_to_list([14, 78, 2, 56, 9]), 10)))
