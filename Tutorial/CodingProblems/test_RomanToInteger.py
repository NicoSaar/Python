import RomanToInteger
import unittest


class testRomanToInt(unittest.TestCase):
    def testRomanToInt1(self):
        self.assertEquals(RomanToInteger.romanToInt("III"), 3)

    def testRomanToInt2(self):
        self.assertEquals(RomanToInteger.romanToInt("LVIII"), 58)

    def testRomanToInt3(self):
        self.assertEquals(RomanToInteger.romanToInt("MCMXCIV"), 1994)

    def testRomanToInt4(self):
        self.assertEquals(RomanToInteger.romanToInt("IV"), 4)
