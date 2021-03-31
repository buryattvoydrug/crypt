import random
import string
import unittest
import rsa


class rsaTestCase(unittest.TestCase):
    def test_gcd(self):
        cases = [
            (12, 15, 3),
            (3, 7, 1)
        ]
        for i, (a, b, c) in enumerate(cases):
            with self.subTest(case=i, a=a, c=c):
                self.assertEqual(c, rsa.gcd(
                    a, b=b))

    def test_multiplicative_inverse(self):
        cases = [
            (7, 40, 23)
        ]
        for i, (e, phi, res) in enumerate(cases):
            with self.subTest(case=i, e=e, res=res):
                self.assertEqual(res, rsa.multiplicative_inverse(
                    e, phi=phi))


if __name__ == '__main__':
    unittest.main()
