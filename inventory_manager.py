#lab 8

import json
import os
from product import Product
from inventory import Inventory

FILENAME = "inventory.json"

def load_inventory():
    inventory = Inventory()
    if not os.path.exists(FILENAME):
        print(f"{FILENAME} not found. Starting with an empty inventory.")
        return inventory
    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)
        for item in data:
            product = Product(item["id"], item["name"], item["price"], item["stock"])
            inventory.add_product(product)
        print("Inventory loaded successfully.")
    except json.JSONDecodeError:
        print(f"{FILENAME} is empty or invalid. Starting with an empty inventory.")
    return inventory


def save_inventory(inventory):
    data = [product.to_dict() for product in inventory.get_products()]
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)


 
 
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
            inventory.display_all()
 
        elif option == "2":
            print("Add New Product")
            product_id = input("Product ID: ").strip()
            if inventory.search_product(product_id) is not None:
                print("Product ID already exists.")
            else:
                name = input("Product Name: ").strip()
                price = get_float("Price: ")
                stock = get_int("Stock Quantity: ")
                new_product = Product(product_id, name, price, stock)
                inventory.add_product(new_product)
                print("Product added successfully!")
 
        elif option == "3":
            print("Update Stock")
            product_id = input("Enter Product ID: ").strip()
            product = inventory.search_product(product_id)
            if product is None:
                print("Product not found.")
            else:
                print("Product Found:")
                print(f"Name: {product.get_name()}")
                print(f"Current Stock: {product.get_stock()}")
                new_stock = get_int("New Stock Quantity: ")
                inventory.update_stock(product_id, new_stock)
                print("Stock updated successfully!")
 
        elif option == "4":
            print("Search Product")
            product_id = input("Enter Product ID: ").strip()
            product = inventory.search_product(product_id)
            if product is None:
                print("Product not found.")
            else:
                print("Product Found")
                print("-" * 48)
                print(f"ID: {product.get_product_id()}")
                print(f"Name: {product.get_name()}")
                print(f"Price: ${product.get_price():.2f}")
                print(f"Stock: {product.get_stock()}")
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


