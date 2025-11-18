# GitHub: https://github.com/katie8331/lab11-AT-KB
# Partner 1: Isabel Tejeda
# Partner 2: Katie Brisson
import unittest
import calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(3, 4), 7)
        self.assertEqual(calculator.add(-2, 5), 3)
    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.subtract(10, 3), 7)
        self.assertEqual(calculator.subtract(3, 10), -7)
    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.multiply(3, 5), 15)
        self.assertEqual(calculator.multiply(-2, 4), -8)
    def test_divide(self): # 3 assertions
        self.assertEqual(calculator.divide(2, 10), 5)
        self.assertAlmostEqual(calculator.divide(4, 10), 2.5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(calculator.logarithm(10, 100), 2.0)
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(10, -5)
        with self.assertRaises(ValueError):
            calculator.logarithm(10, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(-3, -4), 5)

    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(calculator.square_root(16), 4)
        with self.assertRaises(ValueError):
            calculator.square_root(-9)

# Do not touch this
if __name__ == "__main__":
    unittest.main()