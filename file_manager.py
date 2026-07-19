import csv
import os
import json

from product import Product, InvalidPriceError

filename = "shop.csv"

# Custom decorator used for logging function activity
def log_action(func):

    def wrapper(*args, **kwargs):

        print(f"\n[LOG] Function '{func.__name__}' started.")

        result = func(*args, **kwargs)

        print(f"[LOG] Function '{func.__name__}' finished.\n")

        return result

    return wrapper


# Step 1: Add product to CSV
@log_action
def csv_add(row_data):

    file_exists = os.path.isfile(filename)
    file_empty = os.path.getsize(filename) == 0 if file_exists else True

    with open(filename, mode="a", newline="", encoding="utf-8") as file:

        fieldnames = ["product_name", "product_price", "product_quantity"]

        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header if file is empty
        if not file_exists or file_empty:
            csv_writer.writeheader()

        csv_writer.writerow(row_data)


# Step 2: Read products and calculate total
def csv_reading():

    if not os.path.isfile(filename):

        print("CSV file not found!")
        return

    total_expenditure = 0

    with open(filename, mode="r", newline="", encoding="utf-8") as file:

        csv_reader = csv.DictReader(file)

        for row in csv_reader:

            product_name = row["product_name"]
            product_price = float(row["product_price"])
            product_quantity = int(row["product_quantity"])

            total_expenditure += product_price * product_quantity

            product = Product(
                product_name,
                product_price,
                product_quantity
            )

            product.display_product()

    print(f"Total expenditure : {total_expenditure}")


# Step 3: Update product
@log_action
def csv_update():

    if not os.path.isfile(filename):

        print("CSV file not found!")
        return

    product_name = input("\nUpdating product name : ")

    try:

        new_price = float(input("Updating product price : "))

        if new_price <= 0:
            raise InvalidPriceError

    except ValueError:

        print("Invalid price!")
        return

    except InvalidPriceError:

        print("Price must be greater than 0!")
        return

    new_value = []
    is_updated = False

    with open(filename, mode="r", newline="", encoding="utf-8") as file:

        csv_reader = csv.DictReader(file)

        for row in csv_reader:

            if row["product_name"] == product_name:

                row["product_price"] = new_price
                is_updated = True

            new_value.append(row)

    # Rewrite file
    with open(filename, mode="w", newline="", encoding="utf-8") as file:

        fieldnames = ["product_name", "product_price", "product_quantity"]

        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

        csv_writer.writeheader()
        csv_writer.writerows(new_value)

    if is_updated:

        print(f"\n{product_name} product price successfully updated")

    else:

        print(f"{product_name} product not found")


# Step 4: Delete product
@log_action
def csv_delete():

    if not os.path.isfile(filename):

        print("CSV file not found!")
        return

    product_name = input("Enter product name to delete : ")

    updated_rows = []
    deleted = False

    with open(filename, mode="r", newline="", encoding="utf-8") as file:

        csv_reader = csv.DictReader(file)

        for row in csv_reader:

            if row["product_name"] != product_name:

                updated_rows.append(row)

            else:

                deleted = True

    with open(filename, mode="w", newline="", encoding="utf-8") as file:

        fieldnames = ["product_name", "product_price", "product_quantity"]

        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

        csv_writer.writeheader()
        csv_writer.writerows(updated_rows)

    if deleted:

        print(f"{product_name} deleted successfully.")

    else:

        print("Product not found.")


# Step 5: Sort products by price
def sort_products_by_price():

    if not os.path.isfile(filename):

        print("CSV file not found!")
        return

    products = []

    with open(filename, mode="r", newline="", encoding="utf-8") as file:

        csv_reader = csv.DictReader(file)

        for row in csv_reader:

            products.append(row)

    # Sort products by price using lambda
    sorted_products = sorted(
        products,
        key=lambda product: float(product["product_price"])
    )

    print("\n--- SORTED PRODUCTS ---")

    for product in sorted_products:

        print(
            f"{product['product_name']} - "
            f"{product['product_price']} PLN"
        )


# Step 6: Show expensive products
def expensive_products():

    if not os.path.isfile(filename):

        print("CSV file not found!")
        return

    with open(filename, mode="r", newline="", encoding="utf-8") as file:

        csv_reader = csv.DictReader(file)

        # List comprehension for filtering expensive products
        expensive = [
            row for row in csv_reader
            if float(row["product_price"]) > 100
        ]

    print("\n--- EXPENSIVE PRODUCTS ---")

    if expensive:

        for product in expensive:

            print(
                f"{product['product_name']} - "
                f"{product['product_price']} PLN"
            )

    else:

        print("No expensive products found.")


# Step 7: Generator
# Generator function that returns products one by one
def product_generator():

    if not os.path.isfile(filename):

        print("CSV file not found!")
        return

    with open(filename, mode="r", newline="", encoding="utf-8") as file:

        csv_reader = csv.DictReader(file)

        for row in csv_reader:

            yield row


def show_products_generator():

    print("\n--- PRODUCTS FROM GENERATOR ---")

    for product in product_generator():
        print(
            f"Product: {product['product_name']} | "
            f"Price: {product['product_price']} PLN"
        )


# Step 8: Export to JSON
# Export CSV product data into JSON format
def export_to_json():

    if not os.path.isfile(filename):

        print("CSV file not found!")
        return

    products = []

    with open(filename, mode="r", newline="", encoding="utf-8") as file:

        csv_reader = csv.DictReader(file)

        for row in csv_reader:

            products.append(row)

    with open("products.json", mode="w", encoding="utf-8") as json_file:

        json.dump(products, json_file, indent=4)

    print("Products exported to products.json successfully.")