from shirt import Shirt

shirt_one  = Shirt('red','M','long sleeved',45)
shirt_two  = Shirt('orange','S','short sleeved',30)
print(shirt_one.price)
print(shirt_one.color)
shirt_two.change_price(45)
print(shirt_two.price)
shirt_one.color = 'yellow'
shirt_one.size = 'L'
shirt_one.price = 38 

shirt_one.price = 10
shirt_one.price = 20
shirt_one.color = 'red'
shirt_one.size = 'M'
shirt_one.style = 'long_sleeve'


class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self._price = shirt_price

    def get_price(self):
      return self._price

    def set_price(self, new_price):
      self._price = new_price


shirt_one = Shirt('yellow', 'M', 'long-sleeve', 15)
print(shirt_one.get_price())
shirt_one.set_price(10)