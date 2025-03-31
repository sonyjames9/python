from dataclasses import dataclass

# class Point:
#     x: int
#     y: int
#
#     # 2d points storing 2  values
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     # Official String representation method of an object
#     def __repr__(self):
#         return f"Point(x={self.x}, y={self.y})"
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


@dataclass
class Point:
    x: int
    y: int


p1 = Point(1, 2)
p2 = Point(1, 2)
# p2 = Point(2, 1)
print(p1, p2)
print(p1 == p2)

# CLASS VARS USAGE WITH DATACLASS FUNCTIONALITY

from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class InventoryItem:
    """Class for keeping track of item in inventory"""
    name: str
    unit_price: float
    quantity: int = 0
    sizes: list[str] = field(default_factory=list)
    # sizes: list[str] = field(default=["medium"], init=False)

    class_var: ClassVar[int] = 100

    def total_cost(self) -> float:
        return self.unit_price * self.quantity


help(InventoryItem)


# HOW INHERITANCE IS USED WITH DATACLASS
# BELOW EX OF A DATACLASS INHERITING FROM A NON DATACLASS

class Rectangle:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight



@dataclass
class Square(Rectangle):
    side: float

    def __post_init__(self):
        super().__init__(self.side, self.side)


# REVERSE METHOD RESOLUTION ORDER

@dataclass
class Rect:
    width: int
    length: int


@dataclass
class ColoredRectangle(Rect):
    color: str


rect = ColoredRectangle(10, 10, "blue")


# # INITVAR
# if any InitVar fields are defined, they will also be passed to
# _post_init__() in the order they were defined in the class.
# If no __init__() method is generated, then __post_init__() will
# not automatically be called.
# # If a field is an InitVar, it is considered a pseudo-field called
# an init-only field. As it is not a true field, it is not returned by the module-level
# https://docs.python.org/3/library/dataclasses.html#class-variables

from dataclasses import InitVar


@dataclass
class C:
    i: int
    j: int | None = None
    database: InitVar[str | None] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')


c = C(10, database={"j": "value"})
