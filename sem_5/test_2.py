import unittest
from task_1 import buildTree
from task_2 import isSymetricDFS
from Tree_al import Node, dept_traversal


class TestSortShell(unittest.TestCase):
    def testArea(self):
        self.assertEqual(isSymetricDFS(buildTree([3, 8, 8, 9, 6, 6, 9], 0)), True)
        self.assertEqual(isSymetricDFS(buildTree([3, 8, 8, 9, 6, 6], 0)), False)

    def test_types(self):
        self.assertRaises(TypeError, isSymetricDFS, 1.5)
        self.assertRaises(TypeError, isSymetricDFS, [1, 3, 4, 5])
        self.assertRaises(TypeError, isSymetricDFS, 1)
