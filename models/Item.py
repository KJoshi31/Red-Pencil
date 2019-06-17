class Item:

    def __init__(self, name, price):
        self.name = name
        self.original_price = price
        
        self.sale_price = None
        self.percentage_difference = None
        self.increase_decrease = None

        self.date_price_change = None
        self.sale_status = None


    def get_name(self):
        return self.name

    def get_original_price(self):
        return self.original_price

    def set_sale_price(self, price):

        original_product_price = self.original_price
        sale_price = price
        self.percentage_difference = round(100 - ((sale_price / original_product_price) * 100), 2)

        increase_decrease = ""
        if self.percentage_difference > 0:
            increase_decrease = "increase"
        elif self.percentage_difference < 0:
            increase_decrease = "decrease"

        if increase_decrease != "":
            self.sale_price = price

    def get_sale_price(self):
        return self.sale_price

    def set_date_price_change(self, new_date):
        self.date_price_change = new_date

    def get_date_price_change(self):
        return self.date_price_change

    def get_sale_status(self):
        return self.sale_status

    def set_sale_status(self, value):
        self.sale_status = value
    
def get_items():

    a = Item("hat", 5.00)
    b = Item("shirt", 19.45)
    c = Item("pants", 45.95)
    d = Item("watch", 205.45)    

    items_list = []

    items_list.append(a)
    items_list.append(b)
    items_list.append(c)
    items_list.append(d)

    return items_list

    