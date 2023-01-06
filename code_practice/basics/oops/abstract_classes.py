from abc import ABC, abstractmethod


class Automobile(ABC):

  def __init__(self, name="Automobile"):
    print("Automobile created")

  @abstractmethod
  def start(self):
    print("start of automobile called")

  @abstractmethod
  def stop(self):
    pass

  @abstractmethod
  def drive(self):
    pass


class Car(Automobile):

  def __init__(self, name):
    self.name = name
    print("Car created")

  #

  def start(self):
    super().start()
    print("start of car")


  def stop(self):
    pass

  def drive(self):
    pass


class Bus(Automobile):

  def __init__(self, name):
    self.name = name
    print("Bus created")

  def start(self):
    print("start of bus")

  def stop(self):
    pass

  def drive(self):
    pass


c = Car("Honda")
b = Bus("Honda")
c.start()
