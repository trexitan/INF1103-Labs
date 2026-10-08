#lab 5

inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
]

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

add_product(inventory, "P004", "Monitor", 299.99, 10)
update_stock(inventory, "P002", 50)
print(search_product(inventory, "P004"))
display_all(inventory)
