import unittest
import quicksort


class TestQuicksort(unittest.TestCase):

    def test_happypass(self):
        self.assertEqual([1, 2, 3], quicksort.sort([3, 1, 2]))

    def test_empty(self):
        self.assertEqual([], quicksort.sort([]))

    def test_single(self):
        self.assertEqual([2], quicksort.sort([2]))
