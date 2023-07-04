#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
import random
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test class for the method we want to test"""
    def test_max_int(self):
        """we will test:
            - if the list is empty
            - if it has only one vlue
            - if all values are positive
            - if all values are negative
            - if there is a duplicate max value
            - if the function works with large a list
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6]), 6)
        my_list = [-1, -2, -3, -4, -5, -6]
        self.assertEqual(max_integer(my_list), -1)
        my_list = [-1, -2, -3, -4, -5, -1]
        self.assertEqual(max_integer(my_list), -1)
        my_list = [random.randint(1, 999) for _ in range(99)]
        my_list.append(1000)
        self.assertEqual(max_integer(my_list), 1000)
