# Lav 7 tests
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

p = PhysicalProduct("p010", "Guitar", 350.0, 5, 4.2)
d = DigitalProduct("p011", "Windows 11", 199.0, 50, 4500.0)
print(p.get_fulfilment_info())
print(d.get_fulfilment_info())

light = PhysicalProduct("p020", "Mouse", 25.0, 10, 0.2)
heavy = PhysicalProduct("p021", "Monitor", 300.0, 5, 6.5)
print(f"Light shipping: ${light.calculate_shipping_cost():.2f}")
print(f"Heavy shipping: ${heavy.calculate_shipping_cost():.2f}")

print(p.to_dict())
print(d.to_dict())

p.display_information()
d.display_information()

x = Product("p012", "Mystery", 10.0, 1)   # this should FAIL

