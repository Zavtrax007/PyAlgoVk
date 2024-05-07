import unittest
from task_1 import buildTree
from task_5 import isSameTree
from Tree_al import Node, dept_traversal


class TestIsSameTree(unittest.TestCase):
    def testArea(self):
        self.assertEqual(isSameTree([10, 6, 13, 3, 7, 12, 14]), 42)
        self.assertEqual(isSameTree([10, 6, 13, 3, 7, 12]), 39)
        self.assertEqual(isSameTree([10, 6, 13, 4, 7, 12, 20]), 80)
        self.assertEqual(isSameTree([10]), 100)
        self.assertEqual(isSameTree([10, 2]), 20)
        self.assertEqual(isSameTree([]), None)

    def test_types(self):
        self.assertRaises(TypeError, isSameTree, 1.5, 7)
        self.assertRaises(TypeError, isSameTree, '[1, 3, 4, 5]', [1, 2, 3, 4])
        self.assertRaises(TypeError, isSameTree, 1, 'aloha')
