import unittest
from task_2 import isSubsequence


class TestIsSubsequence(unittest.TestCase):

    def testArea(self):
        self.assertEqual(isSubsequence('uio','quefio'), True)
        self.assertEqual(isSubsequence('iuo','quefio'), False)
        self.assertEqual(isSubsequence('uio','uio'), True)


    def test_types(self):
        self.assertRaises(TypeError, isSubsequence, 'abra', 1.5)
        self.assertRaises(TypeError, isSubsequence, 1, 'abra')
        self.assertRaises(TypeError, isSubsequence, 'abra,'[1])
