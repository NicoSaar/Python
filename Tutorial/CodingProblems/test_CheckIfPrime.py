import unittest
import CheckIfPrime


class TestPrime(unittest.TestCase):

    def test_prime1(self):
        self.assertEqual(CheckIfPrime.main(4), False)

    def test_prime2(self):
        self.assertEqual(CheckIfPrime.main(3), True)

    def test_prime3(self):
        self.assertEqual(CheckIfPrime.main(1), False)

    def test_prime4(self):
        self.assertEqual(CheckIfPrime.main(11), True)

    def test_prime5(self):
        self.assertEqual(CheckIfPrime.main(15), False)

    def test_prime6(self):
        self.assertEqual(CheckIfPrime.main(2137), True)
