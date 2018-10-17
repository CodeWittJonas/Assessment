import unittest
from unittest import TestCase

import task_2 as student_submission


class Task2Test(TestCase):
    """
    Task 2: Data Science
    """

    def test_has_read_csv(self):
        """Has read csv"""
        self.assertTrue(hasattr(student_submission, "read_csv"), "You must declare 'read_csv'")

    def test_read_csv(self):
        """Reads csv file"""
        dognames = student_submission.read_csv('./dognames.csv')

        number_of_lines = len(dognames)
        self.assertEqual(number_of_lines, 1396, 'Unexpected number of lines')

    def test_has_preview_dognames(self):
        """has preview_dognames"""
        self.assertTrue(hasattr(student_submission, "preview_dognames"), "You must declare 'preview_dognames'")

    def test_preview_dognames(self):
        """Test if preview_dognames works"""
        dognames = student_submission.read_csv('./dognames.csv')

        preview = student_submission.preview_dognames(dognames, 1)
        self.assertTrue(isinstance(preview, list), 'The return type of preview_dognames seems wrong')

        preview_all = student_submission.preview_dognames(dognames, 1396)
        self.assertEqual(len(preview_all), 1396, 'The length of the result list seems wrong')

        all_strings = all(isinstance(name, str) for name in preview_all)
        self.assertTrue(all_strings, 'The result list should contain only strings')

    def test_has_dognames_count(self):
        """has dognames_count"""
        self.assertTrue(hasattr(student_submission, "dognames_count"), "You must declare 'dognames_count'")

    def test_dognames_count(self):
        """Test if dognames_count works"""
        dognames = student_submission.read_csv('./dognames.csv')

        count = student_submission.dognames_count(dognames)
        self.assertTrue(isinstance(count, dict), 'The return type of dognames_count seems wrong')

        self.assertEqual(count['Rocky'], 10, 'The counting seems to be wrong')


    def test_has_top_n_dognames(self):
        """has top_n_dognames"""
        self.assertTrue(hasattr(student_submission, "top_n_dognames"), "You must declare 'top_n_dognames'")

    def test_top_n_dognames(self):
        """Test if top_n_dognames works"""
        dognames = student_submission.read_csv('./dognames.csv')

        top_1 = student_submission.top_n_dognames(dognames, 1)
        self.assertTrue(isinstance(top_1, list), 'The return type of top_n_dognames seems wrong')

        self.assertEqual(top_1[0][0], 'Luna', 'The top used dog name seems wrong')

    def test_has_is_valid_row(self):
        """has is_valid_row"""
        self.assertTrue(hasattr(student_submission, "is_valid_row"), "You must declare 'is_valid_row'")

    def test_is_valid_row(self):
        """Test if is_valid_row works"""
        dognames = student_submission.read_csv('./dognames.csv')

        self.assertTrue(student_submission.is_valid_row(dognames[999], year=2007, sex='m'),
                        'Your implementation seems wrong')
        self.assertFalse(student_submission.is_valid_row(dognames[999], year=2006, sex='w'),
                         'Your implementation seems wrong')

    def test_has_filter_dognames(self):
        """has filter_dognames"""
        self.assertTrue(hasattr(student_submission, "filter_dognames"), "You must declare 'filter_dognames'")

    def test_filter_dognames(self):
        """Test if filter_dognames works"""
        dognames = student_submission.read_csv('./dognames.csv')

        unfiltered = student_submission.filter_dognames(dognames)
        self.assertTrue(isinstance(unfiltered, list), 'The return type of filter_dognames seems wrong')

        self.assertEqual(len(student_submission.filter_dognames(dognames, year=2004)), 98,
                         'Your implementation seems wrong')


if __name__ == '__main__':
    unittest.main(verbosity=2)
