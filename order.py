from product import Product
from order_line import OrderLine

class Order:
    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)   # the Order CREATES the line
        self.__order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> None:
        for line in self.__order_lines:
            if line.get_product().get_product_id() == product_id.upper():
                self.__order_lines.remove(line)
                return

    def calculate_total(self) -> float:
        total = 0.0
        for line in self.__order_lines:
            total += line.calculate_subtotal()      # ask each line for its subtotal
        return total

    def display_order(self) -> None:
        print(f"Order {self.__order_id}")
        for line in self.__order_lines:
            line.display_information()
        print(f"Total: ${self.calculate_total():.2f}")

    def get_order_lines(self) -> list[OrderLine]:
        return list(self.__order_lines)