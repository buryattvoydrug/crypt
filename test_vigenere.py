import random
import string
import unittest
import vigenere


class vigenereTestCase(unittest.TestCase):
    def test_encrypt(self):
        cases = [
            ('PYTHON', 'A', 'PYTHON'),
            ('python', 'a', 'python'),
            ('ATTACKATDAWN', 'LEMON', 'LXFOPVEFRNHR')
        ]
        for i, (plaintext, keyword, chiphertext) in enumerate(cases):
            with self.subTest(case=i, plaintext=plaintext, chiphertext=chiphertext):
                self.assertEqual(chiphertext, vigenere.encrypt_vigenere(
                    plaintext, keyword=keyword))

    def test_decrypt(self):
        cases = [
            ('PYTHON', 'A', 'PYTHON'),
            ('python', 'a', 'python'),
            ('LXFOPVEFRNHR', 'LEMON', 'ATTACKATDAWN')
        ]
        for i, (chiphertext, keyword, plaintext) in enumerate(cases):
            with self.subTest(case=i, chiphertext=chiphertext, plaintext=plaintext):
                self.assertEqual(plaintext, vigenere.decrypt_vigenere(
                    chiphertext, keyword=keyword))


if __name__ == '__main__':
    unittest.main()
