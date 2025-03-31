class Circle:
    def __init__(self, radius):
        print("Object initiated")
        self._radius = radius

    @property
    def radius(self):
        """Get the radius of the circle"""
        print("Inside radius property")
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set the radius of the circle"""
        print("radius setter")
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @radius.deleter
    def radius(self):
        """Delete setter radius circle"""
        print("Deleted")
        del self._radius

    @property
    def diameter(self):
        """Get the diameter of the circle"""
        return self._radius * 2


c = Circle(5)
print(c.radius)
print(c.diameter)
del c.radius
c.radius = 10  # @radius.setter call
print(c.radius)
print(c.diameter)
