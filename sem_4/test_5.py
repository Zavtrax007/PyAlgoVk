import unittest
from task_5 import groupAn


class TestGroupAn(unittest.TestCase):
    def testArea(self):
        self.assertEqual(groupAn(['eat', 'tea', 'tan', 'ate', 'nat', 'bat', 'eat']),
                         [['eat', 'tea', 'ate', 'eat'], ['tan', 'nat'], ['bat']])
        self.assertEqual(groupAn(['won', 'now', 'aaa', 'ooo', 'ooo']), [['won', 'now'], ['aaa'], ['ooo', 'ooo']])

    def test_types(self):
        self.assertRaises(TypeError, groupAn, 1.5)
        self.assertRaises(TypeError, groupAn, [2, 1])
        self.assertRaises(TypeError, groupAn, 1)
        self.assertRaises(TypeError, groupAn, 'ananas')
