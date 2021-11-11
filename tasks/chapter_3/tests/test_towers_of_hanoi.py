from unittest import TestCase
from towers_of_hanoi import moveDisks

def add_n_items_to_tower(n, tower):
    for i in range(n, 0, -1):
        tower.append(i)

class TestTowersOfHanoi(TestCase):
    def test_1_item(self):
        tower1, tower2, tower3 = [], [], []
        add_n_items_to_tower(1, tower1)

        moveDisks(1, tower1, tower3, tower2)

        self.assertEqual([], tower1)
        self.assertEqual([], tower2)
        self.assertEqual([1], tower3)

    def test_2_item(self):
        tower1, tower2, tower3 = [], [], []
        add_n_items_to_tower(2, tower1)

        moveDisks(2, tower1, tower3, tower2)

        self.assertEqual([], tower1)
        self.assertEqual([], tower2)
        self.assertEqual([2, 1], tower3)

    def test_0_item(self):
        tower1, tower2, tower3 = [], [], []

        moveDisks(0, tower1, tower3, tower2)

        self.assertEqual([], tower1)
        self.assertEqual([], tower2)
        self.assertEqual([], tower3)

    def test_10_item(self):
        tower1, tower2, tower3 = [], [], []

        moveDisks(10, tower1, tower3, tower2)

        self.assertEqual([], tower1)
        self.assertEqual([], tower2)
        self.assertEqual([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], tower3)
