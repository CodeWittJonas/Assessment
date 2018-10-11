import os
import unittest
from unittest import TestCase
from unittest.mock import patch
from recursion_detector import test_recursion


devnull = open(os.devnull, 'w')

# Load once to enable reloading
# Patch input to pass input() values
# Path stdout and stderr to suppress writing to console for the tests
with patch('builtins.input', side_effect=[1,1]):
    with patch('sys.stdout', devnull):
        with patch('sys.stderr', devnull):
            import task_2 as student_submission


class Task2Test(TestCase):
    """
    Task 2
    """

    def test_has_gcd_function(self):
        """Student defined gcd function"""
        self.assertTrue(hasattr(student_submission, "gcd"), "You must declare 'gcd'")

    def test_recursion(self):
        """Test if function is implemented using recursion"""
        self.assertTrue(test_recursion(lambda: student_submission.gcd(1, 2)), "You must implement the 'gcd' function in a recursive manner")

    def test_1_113(self):
        """GCD of 1, 113"""
        result = student_submission.gcd(1, 113)
        self.assertEqual(result, 1, f"gcd implementation seems wrong")

    def test_48_60(self):
        """GCD of 48, 60"""
        result = student_submission.gcd(48, 60)
        self.assertEqual(result, 12, f"gcd implementation seems wrong")


if __name__ == '__main__':
    unittest.main(verbosity=0)
