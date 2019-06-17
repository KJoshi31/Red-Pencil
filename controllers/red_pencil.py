from datetime import date

class RedPencil:

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.product = None
        self.percentage_difference = None

    def load_product(self, product):
        self.product = product

    def set_sale_price(self, new_price):

        original_product_price = self.product.get_original_price()
        sale_price = new_price
        self.percentage_difference = round(100 - ((sale_price / original_product_price) * 100), 2)

        increase_decrease = ""
        if self.percentage_difference > 0:
            increase_decrease = "increase"
        elif self.percentage_difference < 0:
            increase_decrease = "decrease"

        if increase_decrease != "" self.red_pencil_valid():
            self.product.set_sale_price(sale_price)


    def red_pencil_valid(self):
        
        stable_30_days = self.product.date_price_change = None or (self.start_date.days - self.product.get_date_price_change().days >=30)
