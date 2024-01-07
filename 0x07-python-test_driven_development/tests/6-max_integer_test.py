#!/usr/bin/python3
"""Unitest for max int func"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):

    def test_emptylist(self):
        result = max_integer([])
        self.assertIsNone(result, "Empty list should return None")

    def test_all_positive(self):
        result = max_integer([1, 2, 3, 4, 7])
        self.assertEqual(result, 7, "Should return the max positive num")

    def test_all_negative(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1, "Should return the max negative num")

    def test_mixed_numbers(self):
        result = max_integer([-1, 2, -2, 4, -9])
        self.assertEqual(result, 4, "Should return the max positive num")

    def test_duplicate(self):
        result = max_integer([4, 4, 4, 4])
        self.assertEqual(result, 4, "handle lists with duplicate num")

    def test_float(self):
        result = max_integer([9.5, 6.7, 3.5])
        self.assertEqual(result, 9.5, "handle lists with float num")

    def test_mixed_int_float(self):
        result = max_integer([10.6, 9, 6, 4.5])
        self.assertEqual(result, 10.6, "handle lists with mixed nums")


if __name__ == '__main__':
    unittest.main()
