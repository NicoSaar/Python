import unittest
import CheckIfPrime


class TestPrime(unittest.TestCase):

    # prime numbers false
    def test_prime1(self):
        self.assertFalse(CheckIfPrime.main(4))

    def test_prime2(self):
        self.assertFalse(CheckIfPrime.main(15))

    def test_prime3(self):
        self.assertFalse(CheckIfPrime.main(1))

    # Prime numbers true
    def test_prime4(self):
        self.assertTrue(CheckIfPrime.main(11))

    def test_prime5(self):
        self.assertTrue(CheckIfPrime.main(3))

    def test_prime6(self):
        self.assertTrue(CheckIfPrime.main(2137))
