import random
import string
import unittest
import caesar


class CaesarTestCase(unittest.TestCase):
    def test_encrypt(self):
        cases = [
            ('', 0, ''),
            ('python', 0, 'python'),
            ('Python', 0, 'Python'),
            ('PYTHON', 0, 'PYTHON'),
            ('Python3.6', 0, 'Python3.6'),
            ('', 3, ''),
            ('python', 3, 'sbwkrq'),
            ('Python', 3, 'Sbwkrq'),
            ('PYTHON', 3, 'SBWKRQ'),
            ('Python3.6', 3, 'Sbwkrq3.6')
        ]
        for i, (plaintext, shift, chiphertext) in enumerate(cases):
            with self.subTest(case=i, plaintext=plaintext, chiphertext=chiphertext):
                self.assertEqual(chiphertext, caesar.encrypt_caesar(
                    plaintext, shift=shift))

    def test_decrypt(self):
        cases = [
            ('', 0, ''),
            ('python', 0, 'python'),
            ('Python', 0, 'Python'),
            ('PYTHON', 0, 'PYTHON'),
            ('Python3.6', 0, 'Python3.6'),
            ('', 3, ''),
            ('sbwkrq', 3, 'python'),
            ('Sbwkrq', 3, 'Python'),
            ('SBWKRQ', 3, 'PYTHON'),
            ('Sbwkrq3.6', 3, 'Python3.6')
        ]
        for i, (chiphertext, shift, plaintext) in enumerate(cases):
            with self.subTest(case=i, chiphertext=chiphertext, plaintext=plaintext):
                self.assertEqual(plaintext, caesar.decrypt_caesar(
                    chiphertext, shift=shift))


if __name__ == '__main__':
    unittest.main()
