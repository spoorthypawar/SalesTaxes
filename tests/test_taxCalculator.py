import sys
sys.path.append("..")
import unittest
from src.taxCalculator import *

class TestTaxCalculator(unittest.TestCase):

    def test_basicTaxCalculator(self):
        self.assertEqual((basicTaxCalculator(14.99)),1.50)
        self.assertEqual((basicTaxCalculator(47.50)),4.75)
        self.assertEqual((basicTaxCalculator(27.99)),2.8)
        self.assertEqual((basicTaxCalculator(18.99)),1.9)

    def test_importTaxCalculator(self):
        self.assertEqual((importTaxCalculator(10.00)),0.5)
        self.assertEqual((importTaxCalculator(47.50)),2.4)
        self.assertEqual((importTaxCalculator(27.99)),1.4)
   
       


if __name__ == '__main__':
    unittest.main()