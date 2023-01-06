from datetime import date


class Student:

  _passing_percentage = 40  # class vars can be private

  def __init__(self, name, age=15, percentage=80):
    self._name = name
    self.age = age
    self.percentage = percentage

  @classmethod
  def fromBirthYear(cls, name, year, percentage):
    return cls(name, (date.today().year - year), percentage)

  def studentDetails(self):
    print(f"name = ", self._name)
    print(f"age = ", self.age)
    print(f"percentage = ", self.percentage)

  def isPassed(self):
    if self.percentage > Student._passing_percentage:
      print("Student is passed")
    else:
      print("Student not passed")

  @staticmethod
  def welcomeToSchool():
    print("Welcome")

  @staticmethod
  def isTeen(age):
    return age > 16


s1 = Student("User1")
s1 = Student.fromBirthYear("User1", 1970, 85)
# print(s1.__name) #This is not allowed, you cannot access __name outside the class
print(s1._Student_name)
print(s1._Student_passing_percentage)
s1.studentDetails()
# s1.isPassed()
