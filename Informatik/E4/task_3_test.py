import os
import unittest
from unittest import TestCase
from unittest.mock import patch, mock_open

devnull = open(os.devnull, 'w')

# Load once to enable reloading
# Patch input to pass input() values
# Path stdout and stderr to suppress writing to console for the tests
with patch('builtins.input', side_effect=[]):
    with patch('sys.stdout', devnull):
        with patch('sys.stderr', devnull):
            import task_3 as student_submission

lorem_ipsum_filename = 'lorem-ipsum.txt'

with open(lorem_ipsum_filename) as lorem_file:
    lorem = lorem_file.read()


class Task3Test(TestCase):
    """
    Task 3
    """

    def test_has_search_text_function(self):
        """Student defined search_text function"""
        self.assertTrue(hasattr(student_submission, "search_text"), "You must declare 'search_text'")

    @patch('builtins.open')
    def test_has_student_opened_file(self, mock_open):
        student_submission.search_text(lorem_ipsum_filename, 'lorem')
        self.assertGreaterEqual(mock_open.call_count, 1, "You must call open()")

    @patch('builtins.open', new_callable=mock_open, read_data=lorem)
    def test_count_occurrences(self, mock_file):
        occurrences = student_submission.search_text(lorem_ipsum_filename, 'lorem')
        expected = 21
        self.assertEqual(expected, occurrences,
                         'It seems you are not counting correctly, expected {}, found {}'.format(expected, occurrences))

        occurrences = student_submission.search_text(lorem_ipsum_filename, 'ipsum')
        expected = 24
        self.assertEqual(expected, occurrences,
                         'It seems you are not counting correctly, expected {}, found {}'.format(expected, occurrences))


if __name__ == '__main__':
    unittest.main(verbosity=0)
