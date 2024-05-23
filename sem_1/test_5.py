import unittest
from task_5 import chet


class TestChet(unittest.TestCase):

    def testArea(self):
        self.assertEqual(chet([1, 2, 3, 4, 5, 6, 7]), [2, 4, 6, 1, 5, 3, 7])
        self.assertEqual(chet([3, 6, 7, 3, 4, 4, 6, 10]), [6, 4, 4, 6, 10, 7, 3, 3])

    def test_types(self):
        self.assertRaises(TypeError, chet, 1)
        self.assertRaises(TypeError, chet, '[1, 2, 6]')
        self.assertRaises(TypeError, chet, [1, '2', 6])
