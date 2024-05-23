import unittest
from task_2 import findLis


class TestCountSeq(unittest.TestCase):
    def testArea(self):
        self.assertEqual(findLis([3, 1, 4, 7, 2, 11, 9]), 3)
        self.assertEqual(findLis([3, 1, 4, 7, 9, 17, 7, 2, 11, 9]), 5)
        self.assertEqual(findLis([15, 33, 102, 201, 2, 13, 15, 17, 23, 26]), 6)

    def test_types(self):
        self.assertRaises(TypeError, findLis, 1.5)
        self.assertRaises(TypeError, findLis, '[1, 3, 4, 5]')
        self.assertRaises(TypeError, findLis, 1)

    def test_values(self):
        self.assertRaises(ValueError, findLis, [-30, 15, '44', 12, 'rhz'])
