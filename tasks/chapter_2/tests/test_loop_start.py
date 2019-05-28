from unittest import TestCase
from find_loop_start import find_loop_start as f
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

def find_n_element(list, n):
    cursor = list
    while cursor != None and n > 0:
        n -= 1
        cursor = cursor.next

    return cursor

class TestSumNumbers(TestCase):
    def test_loop_start(self):
        a = convert_array_to_list([1, 2, 3, 4, 5, 6])
        loop_start = find_n_element(a, 1)
        find_n_element(a, 5).next = loop_start
        self.assertEqual(2, f(a).value)

        a = convert_array_to_list([1])
        loop_start = find_n_element(a, 0)
        find_n_element(a, 0).next = loop_start
        self.assertEqual(1, f(a).value)

        self.assertEqual(None, f(None))

        a = convert_array_to_list([1, 2, 3, 4, 5,6 , 7, 8, 9, 10])
        loop_start = find_n_element(a, 0)
        find_n_element(a, 9).next = loop_start
        self.assertEqual(1, f(a).value)

        a = convert_array_to_list([1, 2, 3, 4, 5,6 , 7, 8, 9, 10])
        loop_start = find_n_element(a, 8)
        find_n_element(a, 9).next = loop_start
        self.assertEqual(9, f(a).value)


        a = convert_array_to_list([1, 2, 3, 4, 5,6 , 7, 8, 9, 10])
        loop_start = find_n_element(a, 9)
        find_n_element(a, 9).next = loop_start
        self.assertEqual(10, f(a).value)