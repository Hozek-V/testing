import unittest
import random

def add(a, b):
    return a + b


def multiplication(a, b,):
    return a * b


class TestMathFunctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, 7), 6)
        self.assertEqual(add(3, -6), -3)
        self.assertEqual(add(10, -6), 4)
        self.assertEqual(add(-1, -3), -4)


    def test_multi(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(-1, 1), -1)

if __name__ == '__main__':
    unittest.main()