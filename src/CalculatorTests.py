import unittest


from Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

   # def test_results_property_calculator(self):
    #    calculator = Calculator()
     #   self.assertIsInstance(calculator.result, 8)

    def test_add_method_calulator(self):
        self.assertEqual(self.calculator.addition(4,4), 8)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtraction(4,4), 0)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(4,4), 16)

    def test_division_method_calculator(self):
        self.assertEqual(self.calculator.divide(10, 2 ), 5)

    def test_sqrt_method_calculator(self):
        self.assertEqual(self.calculator.sqrt(25), 5)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(25), 625)

if __name__ == '__main__':
    unittest.main()
