#!/usr/bin/env python3
"""
Tests for the calculator module.
"""

import unittest
from calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""
    
    def test_add(self):
        """Test addition."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(2.5, 3.5), 6.0)
    
    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(10, 10), 0)
        self.assertEqual(subtract(7.5, 2.5), 5.0)
    
    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(2.5, 4), 10.0)
    
    def test_divide(self):
        """Test division."""
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(10, 4), 2.5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(7.5, 2.5), 3.0)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))


if __name__ == "__main__":
    unittest.main()
