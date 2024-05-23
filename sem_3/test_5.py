import unittest
from collections import deque
from task_5 import isPalindromeP


class TestIsPalindromeP(unittest.TestCase):

    def testArea(self):
        self.assertEqual(isPalindromeP('aba'), True)
        self.assertEqual(isPalindromeP('abrba'), True)
        self.assertEqual(isPalindromeP('abraba'), False)
        self.assertEqual(isPalindromeP('moloko'), False)



    def test_types(self):
        self.assertRaises(TypeError, isPalindromeP, 1.5)
        self.assertRaises(TypeError, isPalindromeP, 1)
        self.assertRaises(TypeError, isPalindromeP, [1])
