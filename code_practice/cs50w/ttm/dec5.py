from dataclasses import dataclass

# class Product:
    # def __init__(self, name: str, price: float, quantity: int = 0):
    #     self.name = name
    #     self.price = price
    #     self.quantity = quantity
    #
    # def __repr__(self):
    #     return (f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})")
    #
    # def __eq__(self, other):
    #     if not isinstance(other, Product):
    #         # dont compare against related types
    #         return NotImplemented
    #
    #     return (
    #         self.name == other.name
    #         and self.price == other.price
    #         and self.quantity == other.quantity
    #     )
    #
    #  ALL THE ABOVE METHODS CAN BE REPLACED WITH BELOW, WE DONT NEED TO WRITE
    #  __init__ INIT WRAPPER OR EQUAL METHOD
    # THEY ARE AUTOMATICALLY IMPLEMENTED FOR US
    # USING "@dataclass" DECORATOR we can redefine above class like shown below
@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.price * self.quantity


p1 = Product(name="Laptop", price=1000.0, quantity=3)
p2 = Product(name="Laptop", price=1000.0, quantity=3)
p3 = Product(name="Smartphone", price=500.0, quantity=2)

print(p1) #Product(name='Laptop', price=1000.0, quantity=3)
print(p1.total_cost()) #3000.0
print(p1 == p2) #True
print(p1 == p3) #False

