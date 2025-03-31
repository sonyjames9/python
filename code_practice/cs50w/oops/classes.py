# define class to accept 2d values x and y using oops

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(3, 6)
print(p.x)
print(p.y)