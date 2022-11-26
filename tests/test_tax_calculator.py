import sys
sys.path.append("..")
import unittest
from src.tax_calculator import *

class TestTaxCalculator(unittest.TestCase):

    def test_basicTaxCalculator(self):
        self.assertEqual((basicTaxCalculator(14.99)),1.50)
        self.assertEqual((basicTaxCalculator(47.50)),4.75)
        self.assertEqual((basicTaxCalculator(27.99)),2.8)
        self.assertEqual((basicTaxCalculator(18.99)),1.9)

    def test_importTaxCalculator(self):
        self.assertEqual((importTaxCalculator(10.00)),0.5)
        self.assertEqual((importTaxCalculator(47.50,)),2.4)
        self.assertEqual((importTaxCalculator(27.99)),1.4)

    def test_tax_calculator_usecase1(self):
        inputlist = ["1 book at 12.49","1 music CD at 14.99","1 chocolate bar at 0.85"]
        outputlist=["1 book: 12.49","1 music CD: 16.49","1 chocolate bar: 0.85"]
        data=self.create_tax_data(outputlist,1.5,29.83)
        self.check_tax_data((tax_calculator(inputlist)),data)

    def test_tax_calculator_usecase2(self):
        inputlist = ["1 imported box of chocolates at 10.00", "1 imported bottle of perfume at 47.50"]
        outputlist = ["1 imported box of chocolates: 10.5","1 imported bottle of perfume: 54.65"]
        data=self.create_tax_data(outputlist,7.65,65.15)
        self.check_tax_data((tax_calculator(inputlist)),data)

    def test_tax_calculator_usecase3(self):
        inputlist = ["1 imported bottle of perfume at 27.99","1 bottle of perfume at 18.99","1 packet of headache pills at 9.75","1 box of imported chocolates at 11.25"]
        outputlist = ["1 imported bottle of perfume: 32.19","1 bottle of perfume: 20.89","1 packet of headache pills: 9.75","1 box of imported chocolates: 11.85"]
        data=self.create_tax_data(outputlist,6.70,74.68)
        self.check_tax_data((tax_calculator(inputlist)),data)

    def create_tax_data(self,outputlist, sales_tax,total_price):
        tax_data = TaxData()
        tax_data.set_inputlist(outputlist)
        tax_data.set_sales_tax(sales_tax)
        tax_data.set_total_price(total_price)
        return tax_data

    def check_tax_data(self,actual,expected):
        self.assertEqual(actual.get_inputlist() ,expected.get_inputlist(),"Price of items Mismatch")
        self.assertEqual(actual.get_sales_tax() , expected.get_sales_tax(),"Sales Tax Mismatch")
        self.assertEqual(actual.get_total_price() ,expected.get_total_price(),"Total Price Mismatch")


if __name__ == '__main__':
    unittest.main()