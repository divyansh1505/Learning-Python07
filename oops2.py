class Employee:
    language = "python"    #class attribute
    salary = "1250000"

    def __init__(self, name):   #DUNDER METHOD WHICH IS AUTOMATICALLY CALLED
        self.name = name

        # The __init__ method in Python is a constructor method that is 
        # automatically called when a new instance (object) of a class is 
        # created. It's part of Python's object-oriented programming 
        # (OOP) model and is used to initialize the attributes 
        # (properties) of the object.

    def getInfo(self):
        print(f"The coding language used by {self.name} is {self.language}")
        print(f"The salary given is {self.salary}")

    @staticmethod   # decorator to mark greet as a static method 
    def greet():
        print("Good morning")

shraddha = Employee("sharddha")
shraddha.language = "JavaScript"   #instance attribute

Employee.getInfo(shraddha)
# shraddha.getInfo() - same result as above 
shraddha.greet()
