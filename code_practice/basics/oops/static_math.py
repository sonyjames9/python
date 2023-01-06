
"""
Static method does not require anything like self.

Objects is not required, directly the class name can be used to use the static methods

"""


from os import stat


class Math:

  @staticmethod
  def add5(x):
    return x+5

  @staticmethod
  def add10(x):
    return x+10

  @staticmethod
  def pr():
    print("run")


print(Math.add5(5))
print(Math.add10(5))
Math.pr()
