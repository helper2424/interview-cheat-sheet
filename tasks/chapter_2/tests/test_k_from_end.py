from unittest import TestCase
from find_k_from_end import find_k_from_end as f, find_k_from_end_recursive as f2
from node import Node

def convert_list_to_array(list):
    root = list
    result = []
    while(root != None):
        result.append(root.value)
        root = root.next

    return result


def convert_array_to_list(array):
    if len(array) == 0:
        return None

    root = Node(array[0])
    for i in range(1, len(array)):
        root.add_node(array[i])

    return root

class TestKFromEnd(TestCase):
    def test_non_recursive(self):
        self.assertEqual(None, f(convert_array_to_list([1]), 1))
        self.assertEqual(1, f(convert_array_to_list([1]), 0).value)
        self.assertEqual(5, f(convert_array_to_list([1, 2, 3, 4, 5]), 0).value)
        self.assertEqual(4, f(convert_array_to_list([1, 2, 3, 4, 5]), 1).value)
        self.assertEqual(1, f(convert_array_to_list([1, 2, 3, 4, 5]), 4).value)


    def test_recrusive(self):
        self.assertEqual(None, f2(convert_array_to_list([1]), 1))
        self.assertEqual(1, f2(convert_array_to_list([1]), 0).value)
        self.assertEqual(5, f2(convert_array_to_list([1, 2, 3, 4, 5]), 0).value)
        self.assertEqual(4, f2(convert_array_to_list([1, 2, 3, 4, 5]), 1).value)
        self.assertEqual(1, f2(convert_array_to_list([1, 2, 3, 4, 5]), 4).value)

