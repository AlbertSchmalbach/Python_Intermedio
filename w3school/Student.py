from Person import Person

class Student(Person):
    def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2022)
x.printname()

x.welcome()