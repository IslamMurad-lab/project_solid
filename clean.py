class Item:
    """
    A class to represent an item in the invoice
    
    """
    def __init__(self ,name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_price(self) -> float:
        return self.price * self.quantity
    
class Invoice:
    """
    A class to represent an invoice.
    """
    def __init__(self, customer_name: str, items: list) -> None:
        self.customer_name = customer_name
        self.items = items

    def calculate_total(self) -> float:
        return sum(item.calculate_price() for item in self.items)

    def display_invoice(self) -> None:
        print(f"Invoice for: {self.customer_name}")
        for item in self.items:
            print(f"{item.name}: {item.calculate_price()} USD")
        print(f"Total: {self.calculate_total()} USD")
