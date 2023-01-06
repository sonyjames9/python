class Pet:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age

  def show(self):
    print(f"My name is {self.name} and my age is {self.age}")

  def speak(self):
    print("talk human")


class Cat(Pet):
  def __init__(self, name, age, color) -> None:
    # Reference the super class
    super().__init__(name, age)
    self.color = color

  def show(self):
    print(
        f"My name is {self.name} and my age is {self.age} and my color is {self.color}")

  def speak(self):
    print("Meow")


class Dog(Pet):
  def speak(self):
    print("Bark")


p = Pet("Ammu", 16)
p.show()
p.speak()

c = Cat("Fluff", 5, "white")
c.show()
c.speak()

d = Dog("Tommy", 6)
d.speak()
