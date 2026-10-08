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

inventory = load_inventory()
display_all(inventory)


