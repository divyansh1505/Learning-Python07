class Employee:
       company = "Tesla"
       def show(self):
              print(f"Name is {self.name}, salary is {self.salary}")

# class Programmer:
#        company = "SpaceX"
#        def show(self):
#               print(f"Name is {self.name}, salary is {self.salary}")
#        def showLanguage(self):
#               print(f"{self.name} is good with {self.language}")

class Programmer(Employee):
# Here i inherited programmer from the class Employee, so it will have 
# everything Employee had.
          company = "SpaceX"
          def showLanguage(self):
               print(f"{self.name} is good with {self.language}")

a = Employee()
b = Programmer()

print(a.company, b.company)