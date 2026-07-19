import re

from product import InvalidPriceError


def get_data():

    product_name = input("Product name : ")

    # Regex validation for product name
    if not re.match(r"^[A-Za-z0-9 ]+$", product_name):
        print("Invalid product name!")
        return None

    try:

        product_price = float(input("Product price : "))

        if product_price <= 0:
            # Raise custom exception if price is invalid
            raise InvalidPriceError

        product_quantity = int(input("Product quantity : "))

    except ValueError:
        print("Invalid value entered!")
        return None

    except InvalidPriceError:
        print("Price must be greater than 0!")
        return None

    return {
        "product_name": product_name,
        "product_price": product_price,
        "product_quantity": product_quantity
    }