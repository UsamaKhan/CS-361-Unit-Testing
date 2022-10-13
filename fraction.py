class Fraction(object):
    """Reduced fraction class with integer numerator and denominator."""

    def __init__(self, numerator=0, denominator=1):
        # precondition: if provided, numerator and denominator are integers, denominator is not 0
        # postcondition: self.numerator and self.denominator are stored in reduced terms, with the gcd removed
        # if both arguments are negative, signs cancel and self.numerator, self.denominator will both be positive
        # if denominator is negative and numerator is positive, move the sign to self.numerator; self.denominator
        # should always be positive.
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        # precondition: self is valid
        # postcondition: return "<self.numerator>/<self.denominator>" unless the denominator is 1, then return
        # <self.numerator>
        pass

    # you need not worry about the rest for this lab
    def __float__(self):
        pass

    def __eq__(self, other):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass
