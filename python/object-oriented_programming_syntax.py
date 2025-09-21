# ------------------------------------------------------------
# OOP Example: Shirt Class
# ------------------------------------------------------------
# This program demonstrates how to:
# 1. Define a class with attributes and methods.
# 2. Create objects (instances) from the class.
# 3. Use methods to modify object attributes and compute values.
# 4. Store objects in a collection (list) and iterate over them.
# ------------------------------------------------------------

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
        self.price = new_price

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


# ------------------------------------------------------------
# Example Usage
# ------------------------------------------------------------

# Create a shirt instance
new_shirt = Shirt('red', 'S', 'short sleeve', 15)

# Access attributes
print(new_shirt.color)   # red
print(new_shirt.size)    # S
print(new_shirt.style)   # short sleeve
print(new_shirt.price)   # 15

# Change the price using the method
new_shirt.change_price(10)
print(new_shirt.price)   # 10

# Apply a discount and display the new price
print(new_shirt.discount(0.2))  # 8.0

# ------------------------------------------------------------
# Collection of Shirt objects
# ------------------------------------------------------------
tshirt_collection = []

shirt_one = Shirt('orange', 'M', 'short sleeve', 25)
shirt_two = Shirt('red', 'S', 'short sleeve', 15)
shirt_three = Shirt('purple', 'XL', 'short sleeve', 10)

tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)
tshirt_collection.append(shirt_three)

# Print the color of each shirt in the collection
for shirt in tshirt_collection:
    print(shirt.color)
