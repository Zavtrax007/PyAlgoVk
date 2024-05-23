import unittest
from task_2 import reverseMas, lolRev


class TestReverseMas(unittest.TestCase):

    def testArea(self):
        self.assertEqual(reverseMas([1, 2, 3, 4, 5], 1, 3), [1, 4, 3, 2, 5])
        self.assertEqual(reverseMas([7, 5, 2, 3, 4, 5, 6], 0, 5), [5, 4, 3, 2, 5, 7, 6])

    def test_values(self):
        self.assertRaises(ValueError, reverseMas, [1, 2, 3, 4, 5], -10, 3)
        self.assertRaises(ValueError, reverseMas, [1, 2, 3, 4, 5], 2, 18)

    def test_types(self):
        self.assertRaises(TypeError, reverseMas, 1, 2, 3)
        self.assertRaises(TypeError, reverseMas, [1, 2, 3, 4, 5], '-10', 3)
        self.assertRaises(TypeError, reverseMas, [1, 2, 3, 4, 5], 2, 3.5)


class TestLolRev(unittest.TestCase):

    def testArea(self):
        self.assertEqual(lolRev([1, 2, 3, 4, 5, 6, 7], 3), [4, 5, 6, 7, 1, 2, 3])
        self.assertEqual(lolRev([7, 5, 2, 3, 4, 5, 6], 3), [3, 4, 5, 6, 7, 5, 2])

    def test_values(self):
        self.assertRaises(ValueError, lolRev,[1, 2, 3, 4, 5, 6, 7], 10)
        self.assertRaises(ValueError, lolRev,[1, 2, 3, 4, 5, 6, 7], -3)

    def test_types(self):
        self.assertRaises(TypeError, lolRev, 1, 3)
        self.assertRaises(TypeError, lolRev, [1, 2, 3, 4, 5, 6, 7], 3.5)

