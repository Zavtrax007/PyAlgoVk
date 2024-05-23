import unittest
from task_5 import maxProfit


class TestMaxProfit(unittest.TestCase):
    def testArea(self):
        self.assertEqual(maxProfit([3, 1, 4, 7, 2, 11, 9]), 10)
        self.assertEqual(maxProfit([3, 1, 4, 7, 9, 17, 7, 2, 11, 9]), 16)
        self.assertEqual(maxProfit([15, 33, 102, 201, 2, 13, 15, 17, 23, 26]), 186)

    def test_types(self):
        self.assertRaises(TypeError, maxProfit, 1.5)
        self.assertRaises(TypeError, maxProfit, '[1, 3, 4, 5]')
        self.assertRaises(TypeError, maxProfit, 1)

    def test_values(self):
        self.assertRaises(ValueError, maxProfit, [-30, 15.5, '44', 12, 'rhz'])
        self.assertRaises(ValueError, maxProfit, [3, -1, 4, 7, 2, 11, 9])
