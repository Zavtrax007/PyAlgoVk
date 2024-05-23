import unittest
from task_1 import countSeq


class TestCountSeq(unittest.TestCase):
    def testArea(self):
        self.assertEqual(countSeq(1), 2)
        self.assertEqual(countSeq(5), 15)
        self.assertEqual(countSeq(15), 103)

    def test_types(self):
        self.assertRaises(TypeError, countSeq, 1.5)
        self.assertRaises(TypeError, countSeq, '[1, 3, 4, 5]')
        self.assertRaises(TypeError, countSeq, [])

    def test_values(self):
        self.assertRaises(ValueError, countSeq, -30)
