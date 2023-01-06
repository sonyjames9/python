class Mother:
  def __init__(self):
    self.name = "Mother"

  def print(self):
    print(f"Print of mother class{self.name}")


class Father:
  def __init__(self):
    self.name = "Father"

  def print(self):
    print(f"Print of father class {self.name}")

# If the first inheritance is Father, then print() of father will be called.
# If the first inheritance is Mother, then print() of mother will be called.


class Child(Father, Mother):
  def __init__(self, name):
      self.name = name

  def printChild(self):
    print(f"Name of child is : {self.name}")


c = Child("Child object")
c.print()
