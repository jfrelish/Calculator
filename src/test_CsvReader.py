import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class CsvReaderTests(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_self(self):
        test_self = CsvReader('src/CsvFiles/Unit test Self.csv').data
        for row in test_self:
            self.assertEqual(int(row['row']), 2)
            result = int(row['result'])
            pprint(result)

    def test_addition(self):
        test = CsvReader('src/CsvFiles/Unit Test Addition.csv').data
        for row in test:
            result = int(row['Result'])
            self.assertEqual(self.calculator.addition(row['Value 1'], row['Value 2']), result)
            pprint(test)

    def test_subtraction(self):
        test = CsvReader('/src/CsvFiles/Unit Test Subtraction.csv').data
        for row in test:
            result = int(row['Result'])
            if row['Value 1'] != row['Value 2']:
                self.assertEqual(self.calculator.subtraction(row['Value 2'], row['Value 1']), result)
                pprint(test)
            else:
                self.assertEqual(self.calculator.subtraction(row['Value 1'], row['Value 2']), result)
                pprint(test)

    def test_multiply(self):
        test = CsvReader('/src/CsvFiles/Unit Test Multiplication.csv').data
        for row in test:
            result = int(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            pprint(test)

    def test_divide(self):
        test = CsvReader('/src/CsvFiles/Unit Test Division.csv').data
        for row in test:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.divide(row['Value 2'], row['Value 1']), result)
            pprint(test)

    def test_sqrt(self):
        test = CsvReader('/src/CsvFiles/Unit Test Square Root.csv').data
        for row in test:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.sqrt(row['Value 1']), result)
            pprint(test)

    def test_square(self):
        test = CsvReader('/src/CsvFiles/Unit Test Square.csv').data
        for row in test:
            result = int(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            pprint(test)


if __name__ == '__main__':
         unittest.main()