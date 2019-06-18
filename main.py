from controllers.red_pencil import RedPencil
from models.Item import *
from datetime import date


start_date = date(2019,3,1)
end_date = date(2019,3,31)

a = Item("hat", 15.00)
red_pencil = RedPencil(start_date,end_date)


red_pencil.load_product(a)

red_pencil.set_price(11.00)

red_pencil.red_pencil_valid()

print(red_pencil.increase_decrease)
print(red_pencil.percentage_difference)
print(a.get_sale_status())