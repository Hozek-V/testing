import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class TestCalculatorMethods(unittest.TestCase):
    def setUp(self):
        # Inicializácia inštancie kalkulačky pre každý test
        self.calculator = Calculator()
    # def setUpClass(cls):

    def tearDown(self):
        # Vyčistenie po každom teste (ak by bolo niečo potrebné)
        pass
    # def tearDownClass(cls):

    def test_add(self):
        result = self.calculator.add(3, 5)
        self.assertEqual(result, 8, "Sčítanie nefunguje správne")

    def test_subtract(self):
        result = self.calculator.subtract(10, 4)
        self.assertEqual(result, 6, "Odčítanie nefunguje správne")

    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6, "Násobenie nefunguje správne")

    def test_divide(self):
        result = self.calculator.divide(8, 2)
        self.assertEqual(result, 4, "Delenie nefunguje správne")

        # Test delenia nulou
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)


if __name__ == '__main__':
    unittest.main()