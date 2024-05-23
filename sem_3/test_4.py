import unittest
from collections import deque
from task_4 import isPalindromeStack


class TestIsPalindromeStack(unittest.TestCase):

    def testArea(self):
        self.assertEqual(isPalindromeStack('aba'), True)
        self.assertEqual(isPalindromeStack('abrba'), True)
        self.assertEqual(isPalindromeStack('abraba'), False)
        self.assertEqual(isPalindromeStack('moloko'), False)



    def test_types(self):
        self.assertRaises(TypeError, isPalindromeStack, 1.5)
        self.assertRaises(TypeError, isPalindromeStack, 1)
        self.assertRaises(TypeError, isPalindromeStack, [1])
