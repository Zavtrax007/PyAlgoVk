import unittest
from task_3 import isTree

gr = {1: [2, 3, 4], 2: [1], 3: [1], 4: [1, 5, 6], 5: [4], 6: [4]}
gr1 = {1: [2, 3, 4], 2: [1, 5], 3: [1], 4: [1, 5, 6], 5: [4, 2], 6: [4]}


class TestCountSeq(unittest.TestCase):
    def testArea(self):
        self.assertEqual(isTree(gr, 1), True)
        self.assertEqual(isTree(gr1, 1), False)

    def test_types(self):
        self.assertRaises(TypeError, isTree, 1.6, 3)
        self.assertRaises(TypeError, isTree, [1, 3, 4, 5], 3)
        self.assertRaises(TypeError, isTree, gr, 100)
