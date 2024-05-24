import unittest
from task_1 import findConnectedComp


class TestFindConnectedComp(unittest.TestCase):
    def testArea(self):
        self.assertEqual(findConnectedComp({1: [2, 3], 2: [1, 3], 3: [1, 2], 4: [5], 5: [4]}),
                         {1: 1, 2: 1, 3: 1, 4: 2, 5: 2})
        self.assertEqual(
            findConnectedComp({1: [2, 3, 7], 2: [1, 3], 3: [1, 2], 4: [5], 5: [4], 6: [8], 7: [1], 8: [6]}),
            {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 1, 8: 3})

    def test_types(self):
        self.assertRaises(TypeError, findConnectedComp, 1.6)
        self.assertRaises(TypeError, findConnectedComp, [1, 3, 4, 5])
        self.assertRaises(TypeError, findConnectedComp, 1)
