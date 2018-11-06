from unittest import TestCase

import task_1
import random


class Task1Test(TestCase):
    """
    Task 1: Quicksort
    """
    def test_quickSort_numbersListSortedDescending_numbersListSortedAscending(self):
        numbers_list_sorted_descending = [3, 2, 1]
        self.assertEqual(task_1.quick_sort(numbers_list_sorted_descending), [1, 2, 3])

    def test_quickSort_numbersListContainingNegatives_numbersListSortedAscending(self):
        numbers_list_containing_negatives = [-3, -1, -5, -10, -7]
        self.assertListEqual(task_1.quick_sort(numbers_list_containing_negatives), [-10, -7, -5, -3, -1])

    def test_quickSort_numbersListSmallMargins_numbersListSortedAscending(self):
        numbers_list_small_margins = [10.0000000001, 9.99999999, 9.99999989]
        self.assertEqual(task_1.quick_sort(numbers_list_small_margins), [9.99999989, 9.99999999, 10.0000000001])

    def test_quickSort_numbersListContainingNegativesAndPositives_numbersListSortedAscending(self):
        numbers_list_containing_negatives_and_positives = [-1, 2, 0, -2, 5]
        self.assertEqual(task_1.quick_sort(numbers_list_containing_negatives_and_positives), [-2, -1, 0, 2, 5])

    def test_quickSort_listContainingNone_typeErrorRaised(self):
        list_containing_none = [None]
        self.assertRaises(TypeError, task_1.quick_sort, list_containing_none)

    def test_quickSort_noArgumentProvided_typeErrorRaised(self):
        self.assertRaises(TypeError, task_1.quick_sort)




