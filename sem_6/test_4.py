import unittest
from task_4 import findMaxPathSum
from Tree_al import buildTree

a = []
b = [8, 9, 11, 7, 16, 3, 1]
c = []
d = [7, 6, 3, 1, 45, 5, 1]


class TestFindMaxPathSum(unittest.TestCase):
    def testArea(self):
        self.assertEqual(findMaxPathSum(buildTree(b, 0)), [16, 9, 8, 3, 11])
        self.assertEqual(findMaxPathSum(buildTree(d, 0)), [45, 6, 7, 5, 3])

    def test_types(self):
        self.assertRaises(TypeError, findMaxPathSum, 1.5)
        self.assertRaises(TypeError, findMaxPathSum, [1, 3, 4, 5])
        self.assertRaises(TypeError, findMaxPathSum, 1)
