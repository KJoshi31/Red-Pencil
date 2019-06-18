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

        if self.product.get_sale_price() == None and self.product.get_original_price() == new_price:
            raise Exception('Sale price cannot be same as original price when initially set')

        else:

            original_product_price = self.product.get_original_price()
            sale_price = new_price
            self.percentage_difference = round(100 - ((sale_price / original_product_price) * 100), 2)

            if self.percentage_difference > 0:
                self.increase_decrease = "discount increase"
            
            elif self.percentage_difference < 0:
                self.increase_decrease = "discount decrease"

            if self.increase_decrease != "":
                self.product.set_sale_price(sale_price, self.start_date)

    def red_pencil_valid(self):

        subtracted_dates = self.start_date.day - self.product.get_date_price_change().day

        stable_30_days = None

        if self.product.date_price_change == None:
            stable_30_days = True
        elif subtracted_dates == 0:
            stable_30_days = True
        elif subtracted_dates >= 30:
            stable_30_days = True
        else:
            stable_30_days = False

        valid_percentage = (self.percentage_difference >= 5.00 and self.percentage_difference <=30.00)
        valid_discount_type = self.increase_decrease == 'discount increase' 


        if self.product.get_original_price() == self.product.get_sale_price() :
                self.product.set_sale_status("N/A")
            
        elif self.increase_decrease == 'discount decrease' and self.product.get_sale_status() == 'Red Pencil':
                self.product.set_sale_status("N/A")  

        print("day subtraction: {}".format(self.start_date.day - self.product.get_date_price_change().day))
        print("stable for 30 days: {}".format(stable_30_days))
        print("valid percentage: {}".format(valid_percentage))
        print("valid discount type: {}".format(valid_discount_type))

    
    
        
