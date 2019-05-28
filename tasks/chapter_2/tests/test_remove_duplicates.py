from unittest import TestCase
from remove_duplicates_from_linked_list import remove_duplicates as f, remove_duplicates_without_buffer as f2
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
    def test_remove_duplicates(self):
        self.assertEqual([1,2,3,4], convert_list_to_array(f(convert_array_to_list([1,2,1,1,3,3,2,1,1,4,4,4,4]))))
        self.assertEqual([1, 2, 3, 4],
                         convert_list_to_array(f(convert_array_to_list([1, 2, 1, 1, 3, 3, 2, 1, 1, 4, 4, 4, 4]))))
        self.assertEqual([1, 2, 3, 4],
                         convert_list_to_array(f(convert_array_to_list([1, 2, 3, 4]))))
        self.assertEqual([1],
                         convert_list_to_array(f(convert_array_to_list([1]))))
        self.assertEqual([1, 2, 3, 4],
                         convert_list_to_array(f(convert_array_to_list([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2]))))

    def test_remove_duplicates_without_buffer(self):
        self.assertEqual([1,2,3,4], convert_list_to_array(f2(convert_array_to_list([1,2,1,1,3,3,2,1,1,4,4,4,4]))))
        self.assertEqual([1, 2, 3, 4],
                         convert_list_to_array(f2(convert_array_to_list([1, 2, 1, 1, 3, 3, 2, 1, 1, 4, 4, 4, 4]))))
        self.assertEqual([1, 2, 3, 4],
                         convert_list_to_array(f2(convert_array_to_list([1, 2, 3, 4]))))
        self.assertEqual([1],
                         convert_list_to_array(f2(convert_array_to_list([1]))))
        self.assertEqual([1, 2, 3, 4],
                         convert_list_to_array(f2(convert_array_to_list([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2]))))