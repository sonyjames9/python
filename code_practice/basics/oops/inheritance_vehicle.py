class Vehicle:
  def __init__(self, color, maxSpeed):
    self.color = color
    # self.maxSpeed = maxSpeed
    self.__maxSpeed = maxSpeed

  def getMaxSpeed(self):
    return self.__maxSpeed

  def setMaxSpeed(self, maxSpeed):
    self.__maxSpeed = maxSpeed

  def print(self):
    print(f"Color : ", self.color)
    print(f"MaxSpeed : ", self.__maxSpeed)


class Car(Vehicle):
  def __init__(self, color, maxSpeed, gears, isConvertible):
      super().__init__(color, maxSpeed)
      self.gears = gears
      self.isConvertible = isConvertible

  def printCar(self):
    # super().print()
    self.print()
    print(f"Total Gears : ", self.gears)
    print(f"Is Converitble : ", self.isConvertible)


c = Car("red", 15, 3, False)
c.printCar()
