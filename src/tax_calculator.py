import math

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
    percent_of_discount = 5
    tax = item_price*percent_of_discount/100
    taxPrice = math.ceil(tax*20) / 20
    return taxPrice

def basicTaxCalculator(item_price):
    percent_of_discount = 10
    tax = item_price*percent_of_discount/100
    return math.ceil(tax*20) / 20


def getInputData():
    input_item_list = []
    while True:
        data = input( )
        if data == "":
            break
        else:
            input_item_list.append(data)
    return input_item_list

def tax_calculator(input_item_list):
    total_sales_tax = total_item_price = updated_price =  0.0
    exempt_set = ["food", "chocolate", "milk", "bread", "book", "pills","tablet","syrup", 'chocolates']
    tax_data = TaxData()
    updated_list = []

    for item in input_item_list:
        import_tax = sales_tax = 0.00
        words = item.split(" ")
        number_of_items = float(words[0])
        item_price = number_of_items * float(words[-1])

        if "imported" in item:
            import_tax += importTaxCalculator(item_price)
        if any(substring  in item for substring in exempt_set):
            tax_flag = False
        else:
            sales_tax += basicTaxCalculator(item_price)

        inputItem = item.split(" at ")
        updated_price = round(item_price+import_tax+sales_tax,2)
        total_item_price += updated_price

        value = (inputItem[0]+": "+str(updated_price))
        updated_list.append(value)
        total_sales_tax += import_tax + sales_tax

    total=(round(total_item_price,2))
    total_sales_tax=math.ceil(total_sales_tax*20) / 20
    tax_data.set_inputlist(updated_list)
    tax_data.set_sales_tax(total_sales_tax)
    tax_data.set_total_price(total)
    return tax_data

def display_data(data):
    for value in data.get_inputlist():
        print(value)
    print("Sales Taxes:",data.get_sales_tax())
    print("Total:",data.get_total_price())

if __name__ == "__main__":
    input_list = getInputData()
    data = tax_calculator(input_list)
    display_data(data)
