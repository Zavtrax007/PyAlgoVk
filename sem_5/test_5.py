import unittest
from task_1 import buildTree
from task_5 import isSameTree
from Tree_al import Node, dept_traversal

a = [7, 4, 5, 1, 8, 11, 17]
b = [7, 4, 5, 1, 8, 11, 17]
c = [7, 4, 5, 18, 8, 11, 17]
d = [7, 4, 3]


class TestIsSameTree(unittest.TestCase):
    def testArea(self):
        self.assertEqual(isSameTree(buildTree(a, 0), buildTree(b, 0)), True)
        self.assertEqual(isSameTree(buildTree(a, 0), buildTree(c, 0)), False)
        self.assertEqual(isSameTree(buildTree(a, 0), buildTree(d, 0)), False)

    def test_types(self):
        self.assertRaises(TypeError, isSameTree, 1.5, 7)
        self.assertRaises(TypeError, isSameTree, '[1, 3, 4, 5]', [1, 2, 3, 4])
        self.assertRaises(TypeError, isSameTree, 1, 'aloha')
