import unittest
from task3 import numbers


class TestNumber(unittest.TestCase):

    def test_number(self):
        self.assertEqual(numbers(33, 33), 33)
        self.assertEqual(numbers(12, 4), 4)
        self.assertEqual(numbers(4, 12), 4)
        self.assertEqual(numbers(3, 7), 1)
        self.assertEqual(numbers(825894, 654), 6)

    def test_values(self):

        self.assertRaises(ValueError, numbers, -3, -5)
        self.assertRaises(ValueError, numbers, -12, -4)
        self.assertRaises(ValueError, numbers, -35, 5)
        self.assertRaises(ValueError, numbers, 25, 0)

    def test_types(self):

        self.assertRaises(TypeError, numbers, 5+2j, 7+2j)
        self.assertRaises(TypeError, numbers, 'hello', 8)
        self.assertRaises(TypeError, numbers, 2.6, 8.8)
        self.assertRaises(TypeError, numbers, [12, 20, 34], 22)
        self.assertRaises(TypeError, numbers, 4, True)
        self.assertRaises(TypeError, numbers, False, 64)
