import unittest
from task_1 import copyTime


class TestCopyTime(unittest.TestCase):

    def testArea(self):
        self.assertEqual(copyTime(10, 1, 2), 7)
        self.assertEqual(copyTime(10, 3, 5), 20)
        self.assertEqual(copyTime(126, 3, 5), 238)
        self.assertEqual(copyTime(17, 8, 1), 16)
    def test_values(self):
        self.assertRaises(ValueError,copyTime,-10,1,2)
        self.assertRaises(ValueError,copyTime,10,-1,2)
        self.assertRaises(ValueError,copyTime,10,1,-2)

    def test_types(self):
        self.assertRaises(TypeError, copyTime, 10.5, 1, 2)
        self.assertRaises(TypeError, copyTime, 10, 'a', 2)
        self.assertRaises(TypeError, copyTime, 10, 1, [42])