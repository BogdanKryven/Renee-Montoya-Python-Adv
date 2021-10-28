import unittest
from Tests_hometask import functions_to_test


class TestCalc(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(functions_to_test.Calculator.add(8, 7), 15)

    def test_diff(self):
        self.assertEqual(functions_to_test.Calculator.subtract(5, 5), 0)

    def test_divide(self):
        self.assertRaises(ValueError, functions_to_test.Calculator.divide, 5, 0)
        with self.assertRaises(ValueError):
            functions_to_test.Calculator.divide(6, 0)
            functions_to_test.Calculator.divide(-2, 0)
            functions_to_test.Calculator.divide(1221212, 0)
            functions_to_test.Calculator.divide(-114225, 0)
            functions_to_test.Calculator.divide(0, 0)

    def test_multiply(self):
        self.assertEqual(functions_to_test.Calculator.multiply(5, 10), 50)
