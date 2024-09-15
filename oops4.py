class Calculator:          # This line defines a class called Calculator. A class is like a blueprint for creating objects (in this case, calculators that can perform operations like square, cube, etc.).
    def __init__(self, n):
        self.n = n
    
#__init__ is a special method that runs automatically when you create a new object of the class.
# It takes self as the first argument, which refers to the current object of the class.
# It also takes n as a parameter, which will be passed when you create an object (in your case, a number).
# Inside __init__, self.n = n stores the number n as an instance attribute. This means every object created from the class will have its own n value

    def square(self):  
        print(f"The square of the number is {self.n*self.n}")

    def cube(self):
        print(f"The cube of the number is {self.n*self.n*self.n}")

    def squareRoot(self):
        print(f"The squareroot of the number is {self.n**1/2}")

    @staticmethod

    # A static method in Python is a method inside a class that does not depend on the
    # instance of the class. It is bound to the class, not the instance, which means 
    # it can be called without creating an object of the class. A static method cannot 
    # access or modify class attributes or instance attributes.

    def greet():
        print("Hello there!")

input = int(input("Enter the number to be operated : "))

a = Calculator(input)
a.hello()
a.square()     #This calls the square method of the Calculator class for the object a.
a.cube()       #yaha bracket me "input" mt bhardena
a.squareRoot()


# What Happens with __init__:
# When you create the object a = Calculator(input), the __init__ method is automatically called. Here's how it works:

# If you enter, say, 4 as input, it becomes input = 4.
# Then, Calculator(4) is called. The __init__ method takes self (the object a) and n = 4 as arguments.
# Inside __init__, self.n = 4 is executed, so now a.n is 4.
# This means that every method (square, cube, squareRoot) will use 4 for its calculations because self.n refers to 4 for the object a
        