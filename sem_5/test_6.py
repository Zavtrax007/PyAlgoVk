import unittest

from task_6 import unicTree


class TestUnicTree(unittest.TestCase):
    def testArea(self):
        self.assertEqual(unicTree(3), 6)
        self.assertEqual(unicTree(4), 24)
        self.assertEqual(unicTree(5), 120)

    def test_types(self):
        self.assertRaises(TypeError, unicTree, 1.5)
        self.assertRaises(TypeError, unicTree, [1, 2, 3, 4])
        self.assertRaises(TypeError, unicTree, 'aloha')

    def test_values(self):
        self.assertRaises(ValueError, unicTree, -31)
