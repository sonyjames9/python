from datetime import date

# print(str(date.today()))
# print(type(date.today().year))


class Student:

  # Class attr
  passing_percentage = 40

  # def studentDetails(self):
  def __init__(self, name, age=15, percentage=80):
    # self.name = "Sony"  # Instance attribute, its accessible till the lifespan of the instance
    # s1.name
    self.name = name
    self.age = age
    self.percentage = percentage  # attribute accessible in this function
    # self.percentage = 80  # instance attribute using self
    # s1.percentage
    # print('Percentage : ', self.percentage)

  @classmethod
  def fromBirthYear(cls, name, year, percentage):
    return cls(name, (date.today().year - year), percentage)

  def studentDetails(self):
    print(f"name = ", self.name)
    print(f"age = ", self.age)
    print(f"percentage = ", self.percentage)

  def isPassed(self):
    if self.percentage > Student.passing_percentage:
      # check if s1.percentage is greater than Class attribute Student passing percentage
      print("Student is passed")
    else:
      print("Student not passed")

  # Static method, self is not required

  @staticmethod   # Using this decorator, instance knows this is class method and  its not related to object
  def welcomeToSchool():
    print("Welcome")

  @staticmethod
  def isTeen(age):
    return age > 16


s1 = Student("User1")
s1 = Student.fromBirthYear("User1", 1970, 85)
s1.studentDetails()  # Below declaration is same as this line
# Student.studentDetails(s1)  # How python interpret reads the function
# s1.isPassed()
