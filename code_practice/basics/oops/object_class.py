class Circle(object):
  def __init__(self, radius):
      self.radius = radius

# This is object value which will be returned when object is called  
  def __str__(self) -> str:
      return "This is a circle class which takes radius"


c = Circle(2)
print(c)
