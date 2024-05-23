import unittest
from task_3 import pascal, pascal_triangle


class TestCountSeq(unittest.TestCase):
    def testArea(self):
        self.assertEqual(pascal(2),[[1], [1, 1]])
        self.assertEqual(pascal(3), [[1], [1, 1], [1, 2, 1]])
        self.assertEqual(pascal(6), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])

    def test_types(self):
        self.assertRaises(TypeError, pascal, 1.5)
        self.assertRaises(TypeError, pascal, '[1, 3, 4, 5]')
        self.assertRaises(TypeError, pascal, [1, 2, 3])


