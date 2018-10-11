import os
import string
import unittest
from unittest import TestCase
from unittest.mock import patch

devnull = open(os.devnull, 'w')

# Load once to enable reloading
# Patch input to pass input() values
# Path stdout and stderr to suppress writing to console for the tests
with patch('builtins.input', side_effect=[]):
    with patch('sys.stdout', devnull):
        with patch('sys.stderr', devnull):
            import task_4 as student_submission


class Task4Test(TestCase):
    """
    Task 4
    """

    def test_has_encrypt_function(self):
        """Student defined encrypt function"""
        self.assertTrue(hasattr(student_submission, "encrypt"), "You must declare 'encrypt'")

    def test_has_decrypt_function(self):
        """Student defined encrypt function"""
        self.assertTrue(hasattr(student_submission, "decrypt"), "You must declare 'decrypt'")

    def test_encrypt(self):
        """Encryption works"""

        plain_text = 'test'
        alphabet = string.ascii_lowercase

        # Reverse alphabet
        encrypted = student_submission.encrypt(plain_text, alphabet[::-1])
        self.assertEqual(encrypted, 'gvhg', "'Encrypted' value is incorrect")


    def test_decrypt(self):
        """Encryption works"""

        plain_text = 'test'
        alphabet = string.ascii_lowercase

        # Reverse alphabet
        decrypted = student_submission.decrypt('gvhg', alphabet[::-1])
        self.assertEqual(decrypted, plain_text, "'Decrypted' value is incorrect")
        

if __name__ == '__main__':
    unittest.main(verbosity=0)
