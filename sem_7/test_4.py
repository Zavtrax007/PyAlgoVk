import unittest
from task_4 import dijksta

gr = {'a': {'b': 3, 'c': 5}, 'b': {'a': 3, 'c': 2, 'd': 3}, 'c': {'a': 5, 'b': 2, 'd': 1}, 'd': {'b': 3, 'c': 1}}
gr1 = {'a': {'b': 1, 'c': 5}, 'b': {'a': 1, 'c': 2, 'd': 3}, 'c': {'a': 5, 'b': 2, 'd': 1}, 'd': {'b': 3, 'c': 1}}


class TestDijksta(unittest.TestCase):
    def testArea(self):
        self.assertEqual(dijksta(gr, 'a'), {'a': 0, 'b': 3, 'c': 5, 'd': 6})
        self.assertEqual(dijksta(gr1, 'a'), {'a': 0, 'b': 1, 'c': 3, 'd': 4})

    def test_types(self):
        self.assertRaises(TypeError, dijksta, 1.6, 3)
        self.assertRaises(TypeError, dijksta, [1, 3, 4, 5], 3)
        self.assertRaises(TypeError, dijksta, gr, 100)
