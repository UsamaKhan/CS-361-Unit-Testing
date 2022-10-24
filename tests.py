from fraction import Fraction
import unittest


class TestInit(unittest.TestCase):
    # several of these will need to check to see if an exception is raised
    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError, msg="Denominator of zero fails to raise DivByZero"):
            Fraction(1, 0)

    def test_default(self):
        a = Fraction()
        self.assertTrue(a.numerator == 0 & a.denominator == 1,
                        "Fails to initialize correctly with default arguments")

    def test_one_arg(self):
        arg1 = 1
        a = Fraction(arg1)
        self.assertTrue(a.numerator == arg1 & a.denominator == 1,
                        "Fails to initialize correctly with one argument")

    def test_two_arg(self):
        arg1 = 1
        arg2 = 2
        a = Fraction(arg1, arg2)
        self.assertTrue(a.numerator == arg1 & a.denominator == arg2,
                        "Fails to initialize correctly with two arguments")

    # noinspection PyArgumentList
    def test_three_arg(self):
        with self.assertRaises(TypeError, msg="Three args provided"):
            Fraction(1, 2, 3)

    def test_invalid_arg(self):
        with self.assertRaises(TypeError, msg="Invalid argument"):
            Fraction("hello")

    def test_neg_denominator(self):
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
    def test_display_fraction(self):
        a = Fraction(1, 2)
        self.assertEqual("1/2", a.__str__(),
                         "Fails to display fraction as string")

    def test_display_int(self):
        a = Fraction(2, 1)
        self.assertEqual("2", a.__str__(),
                         "Fails to display int when denominator is 1")

    def test_display_neg(self):
        a = Fraction(-1, 2)
        self.assertEqual("-1/2", a.__str__(),
                         "Fails to display negative fraction")
