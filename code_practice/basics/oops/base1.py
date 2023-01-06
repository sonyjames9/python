from tkinter import N


class Student:
  def __init__(self, name, age, grade) -> None:
    self.name = name
    self.age = age
    self.grade = grade

  def get_grade(self):
    return self.grade


class Course:
  def __init__(self, std, max_students) -> None:
    self.std = std
    self.max_students = max_students
    self.students = []

  def add_students(self, student):
    if len(self.students) < self.max_students:
      self.students.append(student)
      return True
    return False

  def get_average_grade(self):
    value = 0
    for student in self.students:
      value += student.get_grade()

    return value / len(self.students)


s1 = Student("Ammu", 5, 80)
s2 = Student("Ammu2", 7, 85)
s3 = Student("Ammu3", 9, 90)

course = Course("Nursery", 2)
course.add_students(s1)
course.add_students(s2)
print(course.students[0].name)
print(course.students[1].name)
print(course.get_average_grade())
