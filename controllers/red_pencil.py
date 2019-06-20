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

    def begin_sale(self):

        if self.red_pencil_valid():
            self.product.set_sale_status("red pencil")

        else:
            if self.product.get_original_price() == self.product.get_sale_price():
                self.product.set_sale_status("N/A")

            elif self.increase_decrease == 'discount decrease' and self.product.get_sale_status() == 'Red Pencil':
                self.product.set_sale_status("N/A")

            if self.product.get_sale_status() == 'red pencil' and self.increase_decrease == 'discount decrease':
                if self.product.get_sale_price() == self.product.get_original_price():
                    self.product.set_sale_status("N/A")
                else:
                    self.product.set_sale_price("other sale")

            if self.percentage_difference >30.0 or self.percentage_difference < 5.0:
                self.product.set_sale_status("other sale")

            sale_days = (self.end_date - self.start_date).days

            if sale_days > 30:
                self.product.set_sale_status("other sale")

            

    def set_price(self, new_price):

        if self.product.get_sale_price() == None and self.product.get_original_price() == new_price:
            raise Exception(
                'Sale price cannot be same as original price when initially set')

        else:

            original_product_price = self.product.get_original_price()
            sale_price = new_price
            self.percentage_difference = round(
                100 - ((sale_price / original_product_price) * 100), 2)

            if self.percentage_difference > 0:
                self.increase_decrease = "discount increase"

            elif self.percentage_difference < 0:
                self.increase_decrease = "discount decrease"

            if self.increase_decrease != "":
                self.product.set_sale_price(sale_price, self.start_date)

    def red_pencil_valid(self):

        subtracted_dates = self.start_date.day - \
            self.product.get_date_price_change().day

        stable_30_days = None

        if self.product.date_price_change == None:
            stable_30_days = True
        elif subtracted_dates == 0:
            stable_30_days = True
        elif subtracted_dates >= 30:
            stable_30_days = True
        else:
            stable_30_days = False

        sale_days = (self.end_date - self.start_date).days

        valid_sale_range = sale_days <=30

        valid_percentage = (self.percentage_difference >=
                            5.00 and self.percentage_difference <= 30.00)


        if self.increase_decrease == 'discount increase' and self.product.get_date_price_change() == None:

            return stable_30_days and valid_percentage and valid_sale_range

        else:
            discount_valid = None


            if self.increase_decrease == 'discount decrease':
                discount_valid = False

            elif self.increase_decrease == 'discount increase':
                discount_valid = True

            return stable_30_days and valid_percentage and valid_sale_range and discount_valid
