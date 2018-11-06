from unittest import TestCase

import task_3


class Task3Test(TestCase):
    """
    Task 3: Accounts
    """
    accs = {}

    def setUp(self):
        self.accs = {'Person 1': 100, 'Person 2': 200}

    def tearDown(self):
        self.accs.clear()

    def test_transferFromTo_validValue_valueTransferred(self):
        accs = self.accs
        accs = task_3.transfer_from_to(accs, 'Person 2', 'Person 1', 50)
        self.assertEqual(accs['Person 1'], 150)
        self.assertEqual(accs['Person 2'], 150)

    def test_transferFromTo_negativeValue_noChange(self):
        accs = self.accs
        accs = task_3.transfer_from_to(accs, 'Person 1', 'Person 2', -50)
        self.assertEqual(accs['Person 1'], 100)
        self.assertEqual(accs['Person 2'], 200)

    def test_transferFromTo_samePerson_noChange(self):
        accs = self.accs
        accs = task_3.transfer_from_to(accs, 'Person 1', 'Person 1', 50)
        self.assertEqual(accs['Person 1'], 100)

    def test_createAccount_validInformation_newAccountAdded(self):
        accs = self.accs
        accs = task_3.create_account(accs, 'Person 3', 50)
        self.assertEqual(len(accs), 3)
        self.assertIs(accs['Person 3'], 50)

    def test_createAccount_existingName_noChange(self):
        accs = self.accs
        accs = task_3.create_account(accs, 'Person 1', 0)
        self.assertEqual(accs['Person 1'], 100)

    def test_createAccount_negativeBalance_noAccountCreated(self):
        accs = self.accs
        accs = task_3.create_account(accs, 'Person 3', -10)
        self.assertEqual(len(accs), 2)
