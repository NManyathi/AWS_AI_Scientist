class Shirt:
    """
    A class to represent a Shirt with color, size, style, and price.
    """

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        """
        Initialize a new Shirt object.
        
        Parameters:
            shirt_color (str): Color of the shirt.
            shirt_size (str): Size of the shirt (e.g., S, M, L, XL).
            shirt_style (str): Style of the shirt (e.g., short sleeve).
            shirt_price (float or int): Price of the shirt.
        """
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        """
        Update the price of the shirt.
        
        Parameters:
            new_price (float or int): The new price to set.
        """
        self.price = new_price * 0.81 # convert dollars to Euros
    
    #shirt_one.change_price(10)

    def discount(self, discount):
        """
        Apply a discount to the shirt price.
        
        Parameters:
            discount (float): Discount percentage as a decimal 
                              (e.g., 0.2 for 20% off).
        
        Returns:
            float: The discounted price.
        """
        return self.price * (1 - discount)
