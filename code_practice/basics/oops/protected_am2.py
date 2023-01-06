class Vehicle:
  def __init__(self, color, maxSpeed):
    self.color = color
    # self.maxSpeed = maxSpeed
    self._maxSpeed = maxSpeed

  def getMaxSpeed(self):
    return self._maxSpeed

  def setMaxSpeed(self, maxSpeed):
    self._maxSpeed = maxSpeed

  def print(self):
    print(f"Color : ", self.color)
    print(f"MaxSpeed : ", self._maxSpeed)


class Car(Vehicle):
  def __init__(self, color, maxSpeed, gears, isConvertible):
      super().__init__(color, maxSpeed)
      self.gears = gears
      self.isConvertible = isConvertible

  def print(self):

    print(f"Color : ", self.color)
    # Protected variables can be accessed outside the class variable
    print(f"MaxSpeed : ", self._maxSpeed)

    print(f"Total Gears : ", self.gears)
    print(f"Is Converitble : ", self.isConvertible)


c = Car("red", 15, 3, False)
c.print()

v = Vehicle("red", 18)
v.print()
# Protected vars can be accessed outside the class
v._maxSpeed = 20
v.print()
