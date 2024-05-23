import unittest
from task_1 import reverseMas


class TestReverseMas(unittest.TestCase):

    def testArea(self):
        self.assertEqual(reverseMas([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(reverseMas([7, 5, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 5, 7])

    def test_types(self):
        self.assertRaises(TypeError, reverseMas, 1.5)
        self.assertRaises(TypeError, reverseMas, 'asd')
        self.assertRaises(TypeError, reverseMas, 1)
