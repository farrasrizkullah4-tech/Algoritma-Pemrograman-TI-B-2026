class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def sambutlah(self):
    print("sambutlah", self.firstname, self.lastname, "sang juara party", self.graduationyear)

x = Student("Ajo", "Balap", 2024)
x.sambutlah()