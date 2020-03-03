import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class CsvReaderTests(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        test_data = CsvReader('src/CsvFiles/Unit Test Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.addition(row['Value 1'], row['Value 2']), result)


    def test_subtraction(self):
        test_data = CsvReader('/src/CsvFiles/Unit Test Subtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            if row['Value 1'] != row['Value 2']:
                self.assertEqual(self.calculator.subtraction(row['Value 2'], row['Value 1']), result)
                pprint(test_data)
            else:
                self.assertEqual(self.calculator.subtraction(row['Value 1'], row['Value 2']), result)
                pprint(test_data)

if __name__ == '__main__':
         unittest.main()