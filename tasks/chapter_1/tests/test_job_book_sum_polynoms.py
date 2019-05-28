from unittest import TestCase
from job_book_sum_polynoms import sum_polynoms as f

class TestSum_polynoms(TestCase):
    def test_sum_polynoms(self):
        self.assertEqual(f(), 1)
