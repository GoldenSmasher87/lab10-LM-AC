# https://github.com/GoldenSmasher87/lab10-LM-AC
# Partner 1: Lucas Mattos
# Partner 2: Abidul Chowdhury
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-4, -6), -10)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)
        self.assertEqual(subtract(-3, -7), 4)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(15, 5), 75)
        self.assertEqual(mul(4, 6), 24)
        self.assertEqual(mul(3, 37), 111)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(4, 8), 2.0)
        self.assertAlmostEqual(div(3, 27), 9.0)
        self.assertAlmostEqual(div(2, 45), 22.5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(3, 9), 2.0)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 5)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(7, 24), 25.0)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
        with self.assertRaises(ValueError):
            square_root(-9)
    #     # Test basic function
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(169), 13.0)
        self.assertAlmostEqual(square_root(25), 5.0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()