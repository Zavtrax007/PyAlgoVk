import unittest
from task_6 import sumCoins


class TestSumСoins(unittest.TestCase):
    def testArea(self):
        self.assertEqual(sumCoins([1, 2, 5], 11), 3)
        self.assertEqual(sumCoins([2], 3), -1)
        self.assertEqual(sumCoins([1, 2, 5], 1163), 234)

    def test_types(self):
        self.assertRaises(TypeError, sumCoins, 1.5, 3)
        self.assertRaises(TypeError, sumCoins, [1, 3, 5], '[1, 3, 4, 5]')
        self.assertRaises(TypeError, sumCoins, 1, '123')

    def test_values(self):
        self.assertRaises(ValueError, sumCoins, [-30, 15.5, '44', 12, 'rhz'], 3)
        self.assertRaises(ValueError, sumCoins, [3, -1, 4, 7, 2, 11, 9], -1)
        self.assertRaises(ValueError, sumCoins, [3, 11, 9], -30)
