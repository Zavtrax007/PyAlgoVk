import unittest
from task_1 import sort_shell


class TestSortShell(unittest.TestCase):
    def testArea(self):
        self.assertEqual(sort_shell([31, 23, 14, 7, 3, 1, 238, 234, 65]), [1, 3, 7, 14, 23, 31, 65, 234, 238])
        self.assertEqual(sort_shell([7, 8, 10, 1, 3, 51, 245, 711]), [1, 3, 7, 8, 10, 51, 245, 711])

    def test_types(self):
        self.assertRaises(TypeError, sort_shell, 1.5)
        self.assertRaises(TypeError, sort_shell, 'asd')
        self.assertRaises(TypeError, sort_shell, 1)
