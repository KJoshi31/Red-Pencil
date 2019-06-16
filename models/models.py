class Item:

    def __init__(self, name, price):
        self.name = name
        self.original_price = price

    def get_name(self):
        return self.name

    def get_original_price(self):
        return self.original_price

    
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

    