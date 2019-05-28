from unittest import TestCase
from check_palindrom import is_palindrom as f
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

class TestChechPalindrom(TestCase):
    def test_check_palindrom(self):
        self.assertTrue(f(convert_array_to_list([1])))
        self.assertTrue(f(None))
        self.assertFalse(f(convert_array_to_list([1, 2])))
        self.assertFalse(f(convert_array_to_list([2, 1])))
        self.assertTrue(f(convert_array_to_list([1,2,1])))
        self.assertTrue(f(convert_array_to_list([1,2,1,2,1])))
        self.assertTrue(f(convert_array_to_list([1,3,5,5,3,1])))
