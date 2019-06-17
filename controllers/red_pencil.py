from datetime import date

class RedPencil:

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.product = None
        self.percentage_difference = None

    def load_product(self, product):
        self.product = product

    def red_pencil_valid(self):
        
        stable_30_days = self.product.date_price_change = None or (self.start_date.days - self.product.get_date_price_change().days >=30)

