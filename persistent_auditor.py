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

product_name = input("Enter Product name: ")
quantity = input("Enter Quantity: ")

if len(orders) == 0:
    order_id = 1001
else:
    last_order = orders[-1]
    order_parts = last_order.split(",")
    order_id = int(order_parts[0]) + 1

new_order = f"{order_id},{product_name},{quantity}"
orders.append(new_order)
print()
print("New Order Added:")
print(new_order)













