from unittest import TestCase

import task_2


class Task2Test(TestCase):
    """
    Task 2: List duplicates
    """
    def test_listDuplicates_listOfNumbers_returnList(self):
        list_of_numbers = [1, 2, 3]
        self.assertIsInstance(task_2.list_duplicates(list_of_numbers), list)

    def test_listDuplicates_listOfNumbers_checkIfListContainsTuples(self):
        list_of_numbers = [1, 2, 3]
        output = task_2.list_duplicates(list_of_numbers)

        for item in output:
            self.assertIsInstance(item, tuple)

    def test_listDuplicates_listOfNumbers_correctIndexesReturned(self):
        list_of_numbers = [1, 2, 1, 2, 3, 4, 5, 6, 7, 4]
        self.assertEqual(task_2.list_duplicates(list_of_numbers), [(1, (0, 2)), (2, (1, 3)), (4, (5, 9))])

    def test_listDuplicates_listContainingNone_typeErrorRaised(self):
        list_containing_none = [None]
        self.assertRaises(TypeError, task_2.list_duplicates(list_containing_none))
