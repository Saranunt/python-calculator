import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add1(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add2(self):
        self.assertEqual(self.calc.add(-6, 6), 0)
    def test_add3(self):
        self.assertEqual(self.calc.add(-6, 6), 0)

    def test_sub1(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
    def test_sub2(self):        
        self.assertEqual(self.calc.subtract(-1, 5), -6)
    def test_sub3(self):
        self.assertEqual(self.calc.subtract(1, 1), 0)

    def test_mul1(self):
        self.assertEqual(self.calc.multiply(2, 1), 2)
    def test_mul2(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)
    def test_mul3(self):
        self.assertEqual(self.calc.multiply(-2, -2), 4)
    
    def test_div1(self):
        self.assertEqual(self.calc.divide(2, 1), 2)
    def test_div2(self):
        self.assertEqual(self.calc.divide(1, 0), ZeroDivisionError)
    def test_div3(self):
        self.assertEqual(self.calc.divide(2, -1), -2)
    
    def test_mod1(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
    def test_mod2(self):
        self.assertRaises(self.calc.modulo(10, 0), ZeroDivisionError)
    def test_mod3(self):
        self.assertEqual(self.calc.modulo(-10, 3), 0)


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()