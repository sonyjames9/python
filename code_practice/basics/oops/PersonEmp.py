""" 
num_of_people is not specific to instance of an class
num_of_people is specific to the class

Now if you move
Person.num_of_people added to init method will keep track of the instances created each time a new object is declared

  def __init__(self, name) -> None:
    Person.num_of_people += 1
    self.name = name

class methods - 
  @classmethod
  def num_of_people(cls):
    return cls.num_of_people()

  @classmethod
  def num_of_people(cls):
    return cls.num_of_people()

self is for objects, above used cls is used for class

"""


class Person:
  num_of_people = 0
  GRAVITY = -9.8

  def __init__(self, name) -> None:
    self.name = name
    # Person.num_of_people += 1
    Person.add_person()

  def __init__(self, name) -> None:
    self.name = name
    # Person.num_of_people += 1
    Person.add_person()

  @classmethod
  def num_of_people_(cls):
    return cls.num_of_people

  @classmethod
  def add_person(cls):
    cls.num_of_people += 1


p1 = Person("AB")
print(p1.num_of_people)
print(Person.num_of_people_())
p2 = Person("CD")
print(p2.num_of_people)
print(Person.num_of_people_())
