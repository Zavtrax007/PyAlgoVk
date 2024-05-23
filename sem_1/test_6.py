import unittest
from task_6 import zeroLast


class TestZeroLast(unittest.TestCase):

    def testArea(self):
        self.assertEqual(zeroLast([0, 0, 1, 0, 3, 12]), [12, 3, 1, 0, 0, 0])
        self.assertEqual(zeroLast([0, 33, 57, 88, 60, 0, 0, 80, 99]), [99, 33, 57, 88, 60, 80, 0, 0, 0])
        self.assertEqual(zeroLast([0, 0, 0, 18, 16, 0, 0, 77, 99]), [99, 77, 16, 18, 0, 0, 0, 0, 0])

    def test_types(self):
        self.assertRaises(TypeError, zeroLast, 1)
        self.assertRaises(TypeError, zeroLast, '[1,2,3]')
        self.assertRaises(TypeError, zeroLast, )
