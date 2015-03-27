from fractions import gcd


class Fraction:

    def __init__(self, numerator, denominator):
        greatest_divisor = gcd(numerator, denominator)
        self.numerator = int(numerator / greatest_divisor)
        self.denominator = int(denominator / greatest_divisor)

    def __str__(self):
        if self.denominator != 1:
            return "{} / {}".format(self.numerator, self.denominator)
        else:
            return str(self.numerator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        numerator = self.numerator * other.denominator + \
            other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - \
            other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator


a = Fraction(1, 2)
b = Fraction(2, 4)

print(a == b)  # True

print(a + b)  # 1
print(a - b)  # 0
print(a * b)  # 1 / 4
