import unittest
from task_2 import feedAnimals


class TestFeedAnimals(unittest.TestCase):
    def testArea(self):
        self.assertEqual(feedAnimals([1, 2, 2], [7, 1]), 2)
        self.assertEqual(feedAnimals([8, 2, 3, 2], [1, 4, 3, 8]), 3)

    def test_types(self):
        self.assertRaises(TypeError, feedAnimals, 1.5, [1, 2])
        self.assertRaises(TypeError, feedAnimals, [2, 1], 'asd')
        self.assertRaises(TypeError, feedAnimals, 1, [])
        self.assertRaises(TypeError, feedAnimals, [1.6, 1], [2])
