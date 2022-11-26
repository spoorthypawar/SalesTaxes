class TaxData:
    def __init__(self):
        self.total_price = 0.0
        self.sales_tax = 0.0
        self.inputlist = []

    def get_total_price(self):
        return self.total_price

    def set_total_price(self, total_price):
        self.total_price = total_price

    def get_sales_tax(self):
        return self.sales_tax

    def set_sales_tax(self, sales_tax):
        self.sales_tax = sales_tax

    def get_inputlist(self):
        return self.inputlist

    def set_inputlist(self, inputlist):
        self.inputlist = inputlist

def importTaxCalculator(item_price):
    return 0.0

def basicTaxCalculator(item_price):
    return 0.0

def tax_calculator(input_item_list):
    return None