import unittest
from datetime import date
from models.item import Item


class TestItemModel(unittest.TestCase):
    
    def test_creation(self):
        a = Item("shirt",31.00)

        self.assertNotEqual(a, None)

    def test_get_name(self):
        a = Item("shirt",31.00)

        self.assertEqual(a.get_name(), "shirt")
        
    def test_get_original_price(self):

        a = Item("shirt",31.00)

        self.assertEqual(a.get_original_price(), 31.00)

    def test_sale_price(self):
        a = Item("shirt",31.00)

        new_date = date(2019, 6,10)

        a.set_sale_price(19.75, new_date)

        self.assertEqual(a.get_sale_price(), 19.75)

    def test_date_price_change(self):

        a = Item("shirt",31.00)

        new_date = date(2019, 6,10)

        a.set_sale_price(19.75, new_date)
    
        self.assertEqual(a.get_date_price_change(), new_date)

    def test_get_sale_status(self):
        a = Item("shirt",31.00)

        self.assertEqual(a.get_sale_status(), "N/A")

    def test_set_sale_status(self):
        a = Item("shirt",31.00)

        a.set_sale_status("red pencil")

        self.assertEqual(a.get_sale_status(), "red pencil")






