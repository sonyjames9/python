class Student:
  # def __init__(self) -> None:
  def __init__(self, name, rollNo) -> None:
      self.name = name
      self.rollNo = rollNo
      subjects = ["A", "B", "C"]


s1 = Student("User1", 10)
s2 = Student("User2", 11)
s3 = Student("User3", 12)
print(s1.__dict__)
print(s2.__dict__)
print(s1,s2)