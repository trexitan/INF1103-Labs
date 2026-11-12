from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order

print("=== Test 1: Association (Supplier - Product) ===")
supplier = Supplier("S001", "TechWorld Pte Ltd", "sales@techworld.com")
p = PhysicalProduct("P010", "Guitar", 350.0, 5, 4.2, supplier)
d = DigitalProduct("P011", "Windows 11", 199.0, 50, 4500.0, supplier)

del supplier    # delete the supplier variable

p.get_supplier().display_information()
d.get_supplier().display_information()

print("\n=== Test 2: Aggregation (Inventory - Product) ===")
supplier2 = Supplier("S002", "GadgetHub", "hello@gadgethub.com")
mouse = PhysicalProduct("P020", "Mouse", 25.0, 10, 0.2, supplier2)   # created BEFORE any inventory

inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(mouse)
print("Inventory A after adding:")
inventory_a.display_all()

inventory_a.remove_product("P020")
print("Inventory A after removing:")
inventory_a.display_all()

print("Can the mouse still be used?")
mouse.display_information()

inventory_b.add_product(mouse)
print("Inventory B after adding the same mouse:")
inventory_b.display_all()

print("\n=== Test 3: Composition (Order - OrderLine) ===")
keyboard = PhysicalProduct("P030", "Keyboard", 45.0, 25, 0.8, supplier2)

order1 = Order("O001")
order1.add_order_line(keyboard, 2)
order1.add_order_line(mouse, 1)
order1.display_order()

order2 = Order("O002")
order2.add_order_line(keyboard, 1)     # same keyboard, different order
order2.display_order()

line_in_order1 = order1.get_order_lines()[0]
line_in_order2 = order2.get_order_lines()[0]
print("Same OrderLine object?", line_in_order1 is line_in_order2)
print("Same Product object?  ", line_in_order1.get_product() is line_in_order2.get_product())

print("\nRemoving the keyboard line from Order 1:")
order1.remove_order_line("P030")
order1.display_order()