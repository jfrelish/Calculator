import unittest
From Calculator import Calculator

class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        Calculator = Calculator()
        self.assertIsInstance(Calculator, Calculator)

    def test_results_property_calculator(self):
        Calculator = Calculator()
        self.assertEqual(Calculator.add(4, 4), 8)


if __name__ == '__main__':
    unittest.main()
