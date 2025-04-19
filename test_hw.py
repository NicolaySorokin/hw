import unittest
from hw import generate_keys, encrypt, decrypt


class TestRSA(unittest.TestCase):
    def setUp(self):
        self.public_key, self.private_key = generate_keys()
        self.message = "Hello"

    def test_key_generation(self):
        self.assertNotEqual(self.public_key, self.private_key)

    def test_encryption_decryption(self):
        ciphertext = encrypt(self.message, self.public_key)
        decrypted_message = decrypt(ciphertext, self.private_key)
        self.assertEqual(self.message, decrypted_message)

    def test_encryption_output(self):
        ciphertext = encrypt(self.message, self.public_key)
        self.assertIsInstance(ciphertext, list)
        self.assertGreater(len(ciphertext), 0)

    def test_decryption_output(self):
        ciphertext = encrypt(self.message, self.public_key)
        decrypted_message = decrypt(ciphertext, self.private_key)
        self.assertIsInstance(decrypted_message, str)

    def test_message_integrity(self):
        ciphertext = encrypt(self.message, self.public_key)
        decrypted_message = decrypt(ciphertext, self.private_key)
        self.assertEqual(self.message, decrypted_message)
