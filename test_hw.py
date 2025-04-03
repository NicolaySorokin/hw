import unittest
from hw import caesar_cipher


class TestCaesar(unittest.TestCase):
    def test_encryption(self):
        self.assertEqual(caesar_cipher("hello", 3), "khoor")
        self.assertEqual(caesar_cipher("abc", 1), "bcd")
        self.assertEqual(caesar_cipher("xyz", 2), "zab")

    def test_case_sensitivity(self):
        self.assertEqual(caesar_cipher("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_large_shifts(self):
        self.assertEqual(caesar_cipher("abcdz", 27), "bcdea")
