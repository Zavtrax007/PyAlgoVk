import unittest
from task_2 import hasCycle


class TestHasCycle(unittest.TestCase):
    def testArea(self):
        self.assertEqual(hasCycle({1: [2], 2: [1, 3], 3: [2, 4, 5], 4: [3, 5], 5: [3]}), True)
        self.assertEqual(
            hasCycle({1: [2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4]}), False)

    def test_types(self):
        self.assertRaises(TypeError, hasCycle, 1.6)
        self.assertRaises(TypeError, hasCycle, [1, 3, 4, 5])
        self.assertRaises(TypeError, hasCycle, 1)
