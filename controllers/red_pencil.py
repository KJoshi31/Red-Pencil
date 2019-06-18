from datetime import date

class RedPencil:

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.product = None
        self.percentage_difference = None
        self.increase_decrease = ""

    def load_product(self, product):
        self.product = product

    def set_price(self, new_price):

        original_product_price = self.product.get_original_price()
        sale_price = new_price
        self.percentage_difference = round(100 - ((sale_price / original_product_price) * 100), 2)

        if self.percentage_difference > 0:
            self.increase_decrease = "discount increase"
        
        elif self.percentage_difference < 0:
            self.increase_decrease = "discount decrease"

        if self.increase_decrease != "":
            if self.product.get_original_price() == new_price:
                self.product.set_sale_status("N/A")
            
            elif self.increase_decrease == 'discount decrease' and self.product.get_sale_status() == 'Red Pencil':
                self.product.set_sale_status("N/A")                

            self.product.set_sale_price(sale_price)


    def red_pencil_valid(self):
        
        stable_30_days = self.product.date_price_change = None or (self.start_date.days - self.product.get_date_price_change().days >=30)
        valid_percentage = (self.percentage_difference >= 5.00 and self.percentage_difference <=30.00)
        valid_discount_type = self.increase_decrease == 'discount increase' 

