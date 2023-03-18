"""Mini-Project: Tests
Sterling Miller, 2023-01-24, CIS 211
"""
import unittest
from buggy import *


class TestMaxRun(unittest.TestCase):

    def test_max_run_example(self):
        self.assertEqual(max_run([1, 2, 2, 2, 3]), [2, 2, 2])

    def test_max_run_example_2(self):
        self.assertEqual(max_run([1, 1, 2, 2, 2, 3]), [2, 2, 2])

    def test_max_run_example_3(self):
        self.assertEqual(max_run([]), [])

    def test_max_run_example_4(self):
        self.assertEqual(max_run([1, 1, 1, 2, 3, 3, 3, 3]), [3, 3, 3, 3])


if __name__ == "__main__":
    unittest.main()
