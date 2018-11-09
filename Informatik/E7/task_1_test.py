from unittest import TestCase

import task_1


class Task1Test(TestCase):
    """
    Task 1: Password Manager
    """

    def setUp(self):
        self.password = task_1.Password("PW1", "User1", "abcd")
        self.manager = task_1.PasswordManager("master-pw")

    def test_password_init(self):
        self.assertEqual(self.password._Password__name, "PW1", "Password object seems wrong")

    def test_password_pretty_str(self):
        self.assertEqual(self.password.pretty_str_password(), "PW1: User1 / abcd")

    def test_password_str(self):
        self.assertEqual(self.password.__str__(), f"PW1: User1 / {'*' * 4}")

    def test_password_manager_init(self):
        self.assertEqual(self.manager._PasswordManager__master_password, "master-pw", "PasswordManager not correctly initialized")
        self.assertFalse(self.manager.unlocked, "Unlocked must initially be False")

    def test_unlock(self):
        self.assertTrue(self.manager.unlock("master-pw"), "Unlock should return True if master password is correct")
        self.assertTrue(self.manager.unlocked, "Unlocked must be True after successful unlocking")

    def test_lock(self):
        self.assertTrue(self.manager.unlock("master-pw"), "Unlock should return True if master password is correct")
        self.manager.lock()
        self.assertFalse(self.manager.unlocked, "Unlocked must be False after locking")

    def test_create_new_password(self):
        self.manager.unlock("master-pw")

        new_pw = self.manager.create_new_password("PW1", "User1", "abcd")
        self.assertEqual(self.manager._PasswordManager__passwords, {new_pw._Password__name: new_pw}, "passwords dictionary seems wrong")

        self.assertEqual(self.manager.create_new_password("PW1", "User3", "xyz"), None, "Creating a password with an existing name should return None")

    def test_update_password(self):
        self.manager.unlock("master-pw")
        self.manager.create_new_password("PW1", "User1", "abcd")

        updated_password = self.manager.update_password("PW1", "User1_edited", "abcdefgh")
        self.assertEqual(updated_password._Password__password, "abcdefgh", "Update password return object seems wrong")

    def test_get_password(self):
        self.manager.unlock("master-pw")

        self.assertEqual(self.manager.get_password("PW1"), None, "Getting a non-existing password should return None")
        new_pw = self.manager.create_new_password("PW1", "User1", "abcd")
        self.assertEqual(self.manager.get_password("PW1"), new_pw, "Get password return value seems wrong")

    def test_list_passwords(self):
        self.manager.unlock("master-pw")

        self.manager.create_new_password("PW1", "User1", "abcd")
        self.manager.create_new_password("PW2", "User2", "efgh")
        self.manager.create_new_password("PW3", "User3", "ijklmnop")

        self.manager.lock()
        self.assertEqual(self.manager.list_passwords(), ["PW1: User1 / ****", "PW2: User2 / ****", "PW3: User3 / ********"], "List passwords in unlocked state should return encoded passwords")
