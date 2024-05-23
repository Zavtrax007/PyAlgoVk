import unittest
from task_7 import delCop


class TestBinarySearchSqrt(unittest.TestCase):

    def testArea(self):
        self.assertEqual(delCop('cdffd'), 'c')
        self.assertEqual(delCop('uioouiouuo'),'uiui' )
        self.assertEqual(delCop('abba'),'' )


    def test_types(self):
        self.assertRaises(TypeError, delCop, 1.5)
        self.assertRaises(TypeError, delCop, 1)
        self.assertRaises(TypeError, delCop, [1])
