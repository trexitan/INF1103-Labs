from product import Product

class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []          

    def add_product(self, product: Product) -> bool:
        if self.find_product(product.get_product_id()) is not None:
            return False              
        self.__products.append(product)
        return True

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id.upper():
                return product
        return None

    def update_stock(self, product_id: str, new_stock: int) -> bool:
        product = self.find_product(product_id)
        if product is None:
            return False
        product.update_stock(new_stock)
        return True

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)
        if product is not None:
            self.__products.remove(product)

    def display_all(self) -> None:
        print("Current Inventory")
        print("-" * 48)
        if len(self.__products) == 0:
            print("No products in inventory.")
        for product in self.__products:
            product.display_information()  
        print("-" * 48)

    def get_products(self) -> list[Product]:
        return list(self.__products)       