import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add(self):
        result = 8
        self.assertEqual(self.calculator.add(3, 5), result)
        self.assertEqual(self.calculator.result, result)
        test_data = CsvReader('/src/CsvFiles/Unit Test Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            pprint(test_data)

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
