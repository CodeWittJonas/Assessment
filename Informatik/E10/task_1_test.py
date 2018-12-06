from unittest import TestCase

import base64_encoder
import task_1


class Task1Test(TestCase):

    def test_base64_encoder_import(self):
        self.assertTrue(hasattr(base64_encoder, "urlsafe_b64encode"), "You must import 'urlsafe_b64encode' in base64_encoder.py")

    def test_base64_encoder_encode(self):
        self.assertTrue(hasattr(base64_encoder, "encode_base64_str"), "You must declare 'encode_base64_str' in base64_encoder.py")

        self.assertEqual(base64_encoder.encode_base64_str("A long Test String!"), "QSBsb25nIFRlc3QgU3RyaW5nIQ==", "encode_base64_str seems wrong")

    def test_task_1_import(self):
        self.assertTrue(hasattr(task_1, "encode"), "You must import the encode_base64_str function as 'encode' in task_1.py")
        self.assertTrue(hasattr(task_1, "decode"), "You must import the decode_base64_str function as 'decode' in task_1.py")

    def test_task_1_encode_decode(self):
        self.assertEqual(task_1.encode("A long Test String!"), "QSBsb25nIFRlc3QgU3RyaW5nIQ==", "encode seems wrong")
        self.assertEqual(task_1.decode("QSBsb25nIFRlc3QgU3RyaW5nIQ=="), "A long Test String!", "decode seems wrong")

    def test_verify(self):
        self.assertTrue(hasattr(task_1, "verify_encoding_decoding"), "You must declare 'verify_encoding_decoding' in task_1.py")

        self.assertTrue(task_1.verify_encoding_decoding("A long Test String!"), "verify_encoding_decoding seems wrong")
