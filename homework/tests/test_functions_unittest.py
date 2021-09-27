import unittest
from functions_to_test import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.classTest = Calculator()

    def test_add(self):
        self.assertEqual(self.classTest.add(2, 3), 5)

    def test_substract(self):
        self.assertEqual(self.classTest.subtract(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(self.classTest.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.classTest.divide(10,2), 5)

    def test_zero_division(self):
        self.assertRaises(ValueError, self.classTest.divide, 2, 0)