import unittest


from Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

   # def test_results_property_calculator(self):
    #    calculator = Calculator()
     #   self.assertIsInstance(calculator.result, 8)

    def test_add_method_calulator(self):
        calculator = Calculator()
        self.assertEqual(calculator.addition(4,4), 8)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtraction(4,4), 0)

    def test_multiply_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(4,4), 16)

    def test_division_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(10, 2 ), 5)

    def test_sqrt_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.sqrt(25), 5)

    def test_square_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.square(25), 625)

if __name__ == '__main__':
    unittest.main()
