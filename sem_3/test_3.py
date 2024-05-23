import unittest
from task_3 import binarySearchSqrt


class TestBinarySearchSqrt(unittest.TestCase):

    def testArea(self):
        self.assertEqual(binarySearchSqrt(36), 6)
        self.assertEqual(binarySearchSqrt(143), 12)
        self.assertEqual(binarySearchSqrt(16), 4)
        self.assertEqual(binarySearchSqrt(28), 5)

    def test_values(self):
        self.assertRaises(ValueError,binarySearchSqrt,-1)
        self.assertRaises(ValueError,binarySearchSqrt,-8)

    def test_types(self):
        self.assertRaises(TypeError, binarySearchSqrt,1.5)
        self.assertRaises(TypeError, binarySearchSqrt,'asd')
        self.assertRaises(TypeError, binarySearchSqrt,[1])
     