import unittest
from task_3 import extraLetter


class TestFeedAnimals(unittest.TestCase):
    def testArea(self):
        self.assertEqual(extraLetter('bbabc', 'bafbcb'), 'f')
        self.assertEqual(extraLetter('uei', 'uoei'), 'o')
        self.assertEqual(extraLetter('uei', 'uei'), '')

    def test_types(self):
        self.assertRaises(TypeError, extraLetter, 1.5, [1, 2])
        self.assertRaises(TypeError, extraLetter, [2, 1], 'asd')
        self.assertRaises(TypeError, extraLetter, 1, [])
