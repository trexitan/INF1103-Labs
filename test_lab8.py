from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

print("=== Test 1: Association (Supplier - Product) ===")
supplier = Supplier("S001", "TechWorld Pte Ltd", "sales@techworld.com")
p = PhysicalProduct("P010", "Guitar", 350.0, 5, 4.2, supplier)
d = DigitalProduct("P011", "Windows 11", 199.0, 50, 4500.0, supplier)

del supplier    # delete the supplier variable

p.get_supplier().display_information()
d.get_supplier().display_information()