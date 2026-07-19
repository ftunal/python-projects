# Custom exception for invalid product prices
class InvalidPriceError(Exception):
    pass

# Product class used for storing product information
class Product:

    def __init__(self, name, price, quantity):

        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product(self):

        print(f"{self.name} - {self.quantity} pieces - {self.price} PLN")