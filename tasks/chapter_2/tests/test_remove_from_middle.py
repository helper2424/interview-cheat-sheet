from unittest import TestCase
from remove_element_from_middle import remove_from_middle as f
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

class TestRemoveDuplicates(TestCase):
    def test_remove_duplicates(self):
        llist = convert_array_to_list([1,2])
        f(llist)
        self.assertEqual([2], convert_list_to_array(llist))

        llist = convert_array_to_list([1,2, 3, 4])
        f(find_n_element(llist, 2))
        self.assertEqual([1, 2, 4], convert_list_to_array(llist))

        llist = convert_array_to_list([1,2, 3, 4, 4, 5, 6, 3,3,3])
        f(find_n_element(llist, 7))
        self.assertEqual([1,2, 3, 4, 4, 5, 6, 3,3], convert_list_to_array(llist))
