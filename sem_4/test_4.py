import unittest
from task_4 import twoSum


class TestTwoSum(unittest.TestCase):
    def testArea(self):
        self.assertEqual(twoSum([1, 3, 4, 6, 5], 11), [3, 4])
        self.assertEqual(twoSum([1, 21, 4, 6, 7], 11), [2, 4])
        self.assertEqual(twoSum([1, 21, 4, 6, 7], 100), [])

    def test_types(self):
        self.assertRaises(TypeError, twoSum, 1.5, [1, 2])
        self.assertRaises(TypeError, twoSum, [2, 1], 'asd')
        self.assertRaises(TypeError, twoSum, 1, [])
