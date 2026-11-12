from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

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