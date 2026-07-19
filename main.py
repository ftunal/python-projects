from validators import get_data

from file_manager import (
    csv_add,
    csv_reading,
    csv_update,
    csv_delete,
    sort_products_by_price,
    expensive_products,
    show_products_generator,
    export_to_json
)
print("Welcome to the Shopping Cart System!")

while True:

    print("\n--- SHOPPING CART MENU ---")
    print("1. Add Product")
    print("2. Show Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Sort Products by Price")
    print("6. Show Expensive Products")
    print("7. Show Generator Products")
    print("8. Export to JSON")
    print("9. Exit")

    choice = input("Select an option : ")

    if choice == "1":

        user_data = get_data()

        if user_data:
            csv_add(user_data)
            print(f"{user_data['product_name']} added successfully")

    elif choice == "2":
        csv_reading()

    elif choice == "3":
        csv_update()

    elif choice == "4":
        csv_delete()

    elif choice == "5":
        sort_products_by_price()

    elif choice == "6":
        expensive_products()

    elif choice == "7":
        show_products_generator()

    elif choice == "8":

        export_to_json()

    elif choice == "9":

        print("Program closed.")
        break

    else:
        print("Invalid option!")