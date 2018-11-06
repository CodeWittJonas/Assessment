from unittest import TestCase

import task_4


class Task4Test(TestCase):
    """
    Task 4: Swap case
    """
    def test_swapCase_allLowerCase_allUpperCase(self):
        test_string = "hello python"
        test_string = task_4.swap_case(test_string)
        self.assertEqual(test_string, "HELLO PYTHON")

    def test_swapCase_allUpperCase_allLowerCase(self):
        test_string = "HELLO UNIT TEST"
        test_string = task_4.swap_case(test_string)
        self.assertEqual(test_string, "hello unit test")

    def test_swapCase_mixedCases_swapedCases(self):
        test_string = "Hello Python"
        test_string = task_4.swap_case(test_string)
        self.assertEqual(test_string, "hELLO pYTHON")

    def test_swapCase_noInput_none(self):
        self.assertIsNone(task_4.swap_case())

