import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add1(self):
        self.assertEqual(self.calc.add(1, 1), 2)
    def test_add2(self):
        self.assertEqual(self.calc.add(-1, 1), 0)
    def test_add3(self):
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_sub1(self):
        self.assertEqual(self.calc.subtract(1, 1), 0)
    def test_sub2(self):        
        self.assertEqual(self.calc.subtract(-1, 1), -2)
    def test_sub3(self):
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_mul1(self):
        self.assertEqual(self.calc.multiply(10, 3), 30)
    def test_mul2(self):
        self.assertEqual(self.calc.multiply(10, 0), 0)
    def test_mul3(self):
        self.assertEqual(self.calc.multiply(-10, -3), 30)
    
    def test_div1(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    def test_div2(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
    def test_div3(self):
        self.assertEqual(self.calc.divide(10, -2), -5)
    
    def test_mod1(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
    def test_mod2(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(10, 0)
    def test_mod3(self):
        self.assertEqual(self.calc.modulo(-10, 3), 2)
    def test_mod4(self):
        self.assertEqual(self.calc.modulo(10, -3), -2)


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()