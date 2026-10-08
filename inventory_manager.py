#lab 5

import json
import os

FILENAME = "inventory.json"

def load_inventory():
    """Load inventory from inventory.json if it exists, else start empty."""
    if os.path.exists(FILENAME):
        print(f"{FILENAME} found.")
        try:
            with open(FILENAME, "r") as file:
                inventory = json.load(file)
            print("Inventory loaded successfully.")
            return inventory
        except json.JSONDecodeError:
            print(f"{FILENAME} is empty or invalid. Starting with an empty inventory.")
            return []
    else:
        print(f"{FILENAME} not found. Starting with an empty inventory.")
        return []

 
def save_inventory(inventory):
    """Save the inventory list to inventory.json."""
    with open(FILENAME, "w") as file:
        json.dump(inventory, file, indent=4)
 

def search_product(inventory, product_id):
    """Return the product dictionary with the matching ID, or None."""
    for product in inventory:
        if product["id"].upper() == product_id.upper():
            return product
    return None

def add_product(inventory, product_id, name, price, stock):
    """Add a new product. Returns False if the ID already exists."""
    if search_product(inventory, product_id) is not None:
        return False
    product = {
        "id": product_id.upper(),
        "name": name,
        "price": price,
        "stock": stock,
    }
    inventory.append(product)
    return True

def update_stock(inventory, product_id, new_stock):
    """Update the stock of a product. Returns False if not found."""
    product = search_product(inventory, product_id)
    if product is None:
        return False
    product["stock"] = new_stock
    return True
 
 
def display_all(inventory):
    """Print every product in the inventory."""
    print("Current Inventory")
    print("-" * 48)
    if len(inventory) == 0:
        print("No products in inventory.")
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | "
              f"Price: ${product['price']:.2f} | Stock: {product['stock']}")
    print("-" * 48)

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Value cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")
 
 
def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Value cannot be negative.")
        except ValueError:
            print("Please enter a whole number.")
 
 
# ---------- Menu System ----------
def show_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")
 
 
def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
 
    inventory = load_inventory()
    show_menu()
 
    while True:
        option = input("Enter option: ").strip()
 
        if option == "1":
            display_all(inventory)
 
        elif option == "2":
            print("Add New Product")
            product_id = input("Product ID: ").strip()
            if search_product(inventory, product_id) is not None:
                print("Product ID already exists.")
            else:
                name = input("Product Name: ").strip()
                price = get_float("Price: ")
                stock = get_int("Stock Quantity: ")
                add_product(inventory, product_id, name, price, stock)
                print("Product added successfully!")
 
        elif option == "3":
            print("Update Stock")
            product_id = input("Enter Product ID: ").strip()
            product = search_product(inventory, product_id)
            if product is None:
                print("Product not found.")
            else:
                print("Product Found:")
                print(f"Name: {product['name']}")
                print(f"Current Stock: {product['stock']}")
                new_stock = get_int("New Stock Quantity: ")
                update_stock(inventory, product_id, new_stock)
                print("Stock updated successfully!")
 
        elif option == "4":
            print("Search Product")
            product_id = input("Enter Product ID: ").strip()
            product = search_product(inventory, product_id)
            if product is None:
                print("Product not found.")
            else:
                print("Product Found")
                print("-" * 48)
                print(f"ID: {product['id']}")
                print(f"Name: {product['name']}")
                print(f"Price: ${product['price']:.2f}")
                print(f"Stock: {product['stock']}")
                print("-" * 48)
 
        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory)
            print(f"Inventory saved successfully to {FILENAME}.")
 
        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
 
        else:
            print("Invalid option. Please enter 1-6.")
 
        print()
 
 
if __name__ == "__main__":
    main()


