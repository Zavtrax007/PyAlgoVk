import unittest
from task_4 import merges_sorted_array


class TestMerges_sorted_array(unittest.TestCase):

    def testArea(self):
        self.assertEqual(merges_sorted_array([1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0], [6, 7, 10, 11]),
                         [1, 2, 3, 4, 5, 6, 6, 7, 7, 10, 11])
        self.assertEqual(merges_sorted_array([1, 2, 4, 4, 7, 0, 0, 0, 0], [6, 7, 10, 11, 100]),
                         [1, 2, 4, 4, 6, 7, 10, 11, 100])

    def test_types(self):
        self.assertRaises(TypeError, merges_sorted_array, '[1, 2, 6]', [3, 4, 5])
        self.assertRaises(TypeError, merges_sorted_array, [1, 2, 6], 1)
