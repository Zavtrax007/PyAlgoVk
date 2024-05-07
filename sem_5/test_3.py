import unittest
from task_1 import buildTree
from task_3 import minDept
from Tree_al import Node, dept_traversal


class TestSortShell(unittest.TestCase):
    def testArea(self):
        self.assertEqual(minDept(buildTree([3, 7, 8, 1, 2, 6, 9], 0)), 3)
        self.assertEqual(minDept(buildTree([3, 7, 8, 1, 2, 6], 0)), 2)

    def test_types(self):
        self.assertRaises(TypeError, minDept, 1.5)
        self.assertRaises(TypeError, minDept, [1, 3, 4, 5])
        self.assertRaises(TypeError, minDept, 1)
