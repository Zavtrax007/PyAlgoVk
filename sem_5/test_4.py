import unittest
from task_1 import buildTree
from task_4 import maxMinMulti
from Tree_al import Node, dept_traversal


class TestSortShell(unittest.TestCase):
    def testArea(self):
        self.assertEqual(maxMinMulti([10, 6, 13, 3, 7, 12, 14]), 42)
        self.assertEqual(maxMinMulti([10, 6, 13, 3, 7, 12]), 39)
        self.assertEqual(maxMinMulti([10, 6, 13, 4, 7, 12, 20]), 80)
        self.assertEqual(maxMinMulti([10]), 100)
        self.assertEqual(maxMinMulti([10, 2]), 20)
        self.assertEqual(maxMinMulti([]), None)

    def test_types(self):
        self.assertRaises(TypeError, maxMinMulti, 1.5)
        self.assertRaises(TypeError, maxMinMulti, '[1, 3, 4, 5]')
        self.assertRaises(TypeError, maxMinMulti, 1)
