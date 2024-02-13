#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
	"""Unittest for max_integer([..])
	"""

	def test_max_integer(self):
		"""Test for max_integer
		"""
		self.assertEqual(max_integer([1, 2, 3, 4]), 4)
		self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
		self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
		self.assertEqual(max_integer([1, 2, 3, 4, 5, 6]), 6)
		self.assertEqual(max_integer([6, 5, 4, 3, 2, 1]), 6)
		self.assertEqual(max_integer([6, 5, 4, 3, 2, 1, 0]), 6)
		self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7]), 7)
		self.assertEqual(max_integer([7, 6, 5, 4, 3, 2, 1]), 7)
		self.assertEqual(max_integer([7, 6, 5, 4, 3, 2, 1, 0]), 7)
		self.assertEqual(max_integer([]), None)
		self.assertEqual(max_integer(), None)
