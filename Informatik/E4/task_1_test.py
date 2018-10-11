import os
import string
import unittest
from unittest import TestCase
from unittest.mock import patch

devnull = open(os.devnull, 'w')

# Load once to enable reloading
# Patch input to pass input() values
# Path stdout and stderr to suppress writing to console for the tests
with patch('builtins.input', side_effect=[0]):
    with patch('sys.stdout', devnull):
        with patch('sys.stderr', devnull):
            import task_1 as student_submission


class Task1Test(TestCase):
    """
    Task 1
    """

    def test_has_handshake_function(self):
        """Student defined handshake function"""
        self.assertTrue(hasattr(student_submission, "handshakes"), "You must declare 'handshake'")

    def test_two_people(self):
        """Handshake for 2 people"""
        result = student_submission.handshakes(2)
        self.assertEqual(result, 1, f"handshakes implementation seems wrong")

    def test_three_people(self):
        """Handshake for 3 people"""
        result = student_submission.handshakes(3)
        self.assertEqual(result, 3, f"handshakes implementation seems wrong")


if __name__ == '__main__':
    unittest.main(verbosity=0)
