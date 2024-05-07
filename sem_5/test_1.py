import unittest
from task_1 import buildTree
from Tree_al import Node, dept_traversal

a = []
b = [8, 9, 11, 7, 16, 3, 1]
c = []
d = [7, 6, 3, 1, 45, 5, 1]


class TestSortShell(unittest.TestCase):
    def testArea(self):
        self.assertEqual(dept_traversal(buildTree(b, 0), a), [7, 9, 16, 8, 3, 11, 1])
        self.assertEqual(dept_traversal(buildTree(d, 0), c), [1, 6, 45, 7, 5, 3, 1])

    def test_types(self):
        self.assertRaises(TypeError, buildTree, 1.5, 1)
        self.assertRaises(TypeError, buildTree, [1, 3, 4, 5], 'asd')
        self.assertRaises(TypeError, buildTree, 1, [1, 3, 4])
