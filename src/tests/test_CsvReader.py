import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class CsvReaderTests(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_csvreader(self):
        self.csv_reader = CsvReader('CsvFiles/Unit test CsvReader.txt')
        self.assertIsInstance(self.csv_reader, CsvReader)
        self.assertEqual((self.csv_reader.data._len_(), 2))

    def test_add(self):
        test_data = CsvReader('CsvFiles/Unit Test Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            pprint(test_data)

    if __name__ == '__main__':
         unittest.main()