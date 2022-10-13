from fraction import Fraction
import unittest


class TestInit(unittest.TestCase):
    # several of these will need to check to see if an exception is raised
    def test_divZero(self):
        with self.assertRaises(ZeroDivisionError, msg="Denominator of zero fails to raise DivByZero"):
            a = Fraction(1, 0)

    def test_default(self):
        a = Fraction()
        self.assertTrue(a.numerator == 0 & a.denominator == 1,
                        "Fails to initialize correctly with default arguments")

    def test_oneArg(self):
        arg1 = 1
        a = Fraction(arg1)
        self.assertTrue(a.numerator == arg1 & a.denominator == 1,
                        "Fails to initialize correctly with one argument")

    def test_twoArg(self):
        arg1 = 1
        arg2 = 2
        a = Fraction(arg1, arg2)
        self.assertTrue(a.numerator == arg1 & a.denominator == arg2,
                        "Fails to initialize correctly with two arguments")

    def test_threeArg(self):
        with self.assertRaises(TypeError, msg="Three args provided"):
            a = Fraction(1, 2, 3)

    def test_invalidArg(self):
        with self.assertRaises(TypeError, msg="Invalid argument"):
            a = Fraction("hello")

    def test_negDenom(self):
        arg1 = 1
        arg2 = -2
        a = Fraction(arg1, arg2)
        self.assertTrue(a.numerator == -arg1 & a.denominator == -arg2,
                        "Fails to move sign from denominator to numerator")

    def test_reduced(self):
        arg1 = 10
        arg2 = 20
        a = Fraction(arg1, arg2)
        self.assertTrue(a.numerator == 1 & a.denominator == 2,
                        "Fails to reduce fraction")


class TestStr(unittest.TestCase):
    def test_displayFraction(self):
        a = Fraction(1, 2)
        self.assertEqual("1/2", a.__str__(),
                         "Fails to display fraction as string")

    def test_displayInt(self):
        a = Fraction(2, 1)
        self.assertEqual("2", a.__str__(),
                         "Fails to display int when denominator is 1")

    def test_displayNeg(self):
        a = Fraction(-1, 2)
        self.assertEqual("-1/2", a.__str__(),
                         "Fails to display negative fraction")

