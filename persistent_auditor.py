# lab 4 
def load_inventory():
    try:
        with open("orders.txt", "r") as file:
            orders = file.readlines()
            return orders
        
    except FileNotFoundError:
        return []


orders = load_inventory()

print("Current Orders:")
print()

for order in orders:
    print(order.strip())
print()












