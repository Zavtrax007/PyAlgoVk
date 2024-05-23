import unittest
from task_3 import iterPascal


class TestCountSeq(unittest.TestCase):
    def testArea(self):
        self.assertEqual(iterPascal(2),[[1], [1, 1]])
        self.assertEqual(iterPascal(3), [[1], [1, 1], [1, 2, 1]])
        self.assertEqual(iterPascal(6), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])

    def test_types(self):
        self.assertRaises(TypeError, iterPascal, 1.5)
        self.assertRaises(TypeError, iterPascal, '[1, 3, 4, 5]')
        self.assertRaises(TypeError, iterPascal, [1, 2, 3])


