class Student:
  name = ""
  rollNo = 12
  """
  oops student user
  """


s1 = Student()
s1.name = "User"
s1.rollNo = 13

s2 = Student()
s2.name = "User2"
s2.rollNo = 14


print(hasattr(s1, 'name'))
print(getattr(s1, "rollNo"))
print(s1.__dict__)
print(s1.__class__)
print(s1.__getattribute__('name'))
print(s1.__module__)
print(s1.__doc__)


