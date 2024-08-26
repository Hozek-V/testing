import unittest


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def simplify(self):
        gcd = self.find_gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    @staticmethod
    def find_gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result


class TestFraction(unittest.TestCase):
    def test_addition(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(str(f1 + f2), "5/6")

    def test_subtraction(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        self.assertEqual(str(f1 - f2), "1/4")

    def test_multiplication(self):
        f1 = Fraction(3, 5)
        f2 = Fraction(2, 3)
        self.assertEqual(str(f1 * f2), "2/5")

    def test_division(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertEqual(str(f1 / f2), "8/9")

    def test_zero_division(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(0, 3)
        with self.assertRaises(ValueError):
            result = f1 / f2


if __name__ == '__main__':
    unittest.main()