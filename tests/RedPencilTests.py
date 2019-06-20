import unittest
from datetime import date
from models.item import Item
from controllers.red_pencil import RedPencil


class TestRedPencilController(unittest.TestCase):

    def test_create_red_pencil(self):
        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 20)

        rp = RedPencil(start_date, end_date)

        self.assertNotEqual(rp, None)
        self.assertEqual(rp.start_date, start_date)
        self.assertEqual(rp.end_date, end_date)
        self.assertEqual(rp.product, None)
        self.assertEqual(rp.percentage_difference, None)
        self.assertEqual(rp.increase_decrease, "")

    def test_load_product(self):

        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 20)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 15.45)

        rp.load_product(a)

        self.assertEqual(id(rp.product), id(a))

    def test_set_sale_price(self):
        
        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 20)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        sale_price = 15.00

        rp.set_price(sale_price)

        self.assertEqual(sale_price, a.get_sale_price())

    def test_sale_original_exception(self):

        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 20)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        sale_price = 20.00

        self.assertRaises(Exception, lambda:rp.set_price(sale_price))

    def test_discount_increase(self):

        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 20)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        rp.set_price(15.00)

        self.assertEqual(rp.increase_decrease, "discount increase")

    def test_discount_decrease(self):

        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 20)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        rp.set_price(21.00)

        self.assertEqual(rp.increase_decrease, "discount decrease")

    def test_date_price_change_default(self):
        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 20)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        self.assertEqual(a.get_date_price_change(), None)

    def test_valid_discount_normal(self):
        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 20)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        rp.set_price(17.00)

        rp.begin_sale()

        self.assertEqual(a.get_sale_status(), "red pencil")

    def test_valid_discount_low(self):
        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 20)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        rp.set_price(19.00)

        rp.begin_sale()

        self.assertEqual(a.get_sale_status(), "red pencil")

    def test_error_discount_low(self):
        
        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 20)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        rp.set_price(19.50)

        rp.begin_sale()

        self.assertNotEqual(a.get_sale_status(), "red pencil")
        self.assertEqual(a.get_sale_status(), "other sale")

    def test_valid_discount_high(self):
        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 20)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        rp.set_price(14.00)

        rp.begin_sale()

        self.assertEqual(a.get_sale_status(), "red pencil")

    def test_error_discount_high(self):
        
        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 20)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        rp.set_price(13.00)

        rp.begin_sale()

        self.assertNotEqual(a.get_sale_status(), "red pencil")
        self.assertEqual(a.get_sale_status(), "other sale")

    def test_valid_sale_range(self):

        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 21)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        rp.set_price(15.00)

        rp.begin_sale()

        self.assertEqual(a.get_sale_status(), 'red pencil')

    def test_sale_range_extended(self):

        start_date = date(2019, 6,1)
        end_date = date(2019, 7, 2)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        rp.set_price(15.00)

        rp.begin_sale()

        self.assertNotEqual(a.get_sale_status(), 'red pencil')
        self.assertEqual(a.get_sale_status(), 'other sale')

    def test_sale_range_30(self):

        start_date = date(2019, 6,1)
        end_date = date(2019, 7, 1)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        rp.set_price(15.00)

        rp.begin_sale()

        self.assertEqual(a.get_sale_status(), 'red pencil')

    def test_price_increase(self):
        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 20)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        rp.set_price(17.00)

        rp.begin_sale()

        rp.set_price(18.00)
        rp.begin_sale()

        self.assertNotEqual(a.get_sale_status(), "red pencil")

    def test_price_decrease(self):
        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 20)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        rp.set_price(17.00)

        rp.begin_sale()

        rp.set_price(15.00)

        self.assertEquals(a.get_sale_status(), 'red pencil')

    def test_invalid_to_red_pencil(self):

        start_date = date(2019, 6,10)
        end_date = date(2019, 6, 20)

        rp = RedPencil(start_date, end_date)

        a = Item("hat", 20.00)

        rp.load_product(a)

        rp.set_price(11.00)

        rp.begin_sale()

        rp.set_price(15.00)

        self.assertEquals(a.get_sale_status(), 'red pencil')