class Class:
    a=1 
    @classmethod   #class decorator
    def show(cls):
        print(f"Class attribute is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    #thats how you return a string
    # This defines a property called name. The @property decorator allows 
    # name to be accessed like an attribute, but behind the scenes, it's 
    # calling this method.
    # name returns a string composed of the fname and lname instance attributes
    # separated by a space.

    @name.setter
    def name(self, value):
        self.fname = value.split(" ") [0]
        self.lname = value.split(" ") [1]
    # This defines a setter for the name property. 
    # When you assign a value to name, this setter is called.
    # It takes the value, splits it by space into a list, and assigns the 
    # first part to self.fname and the second part to self.lname.

e = Class()  #This creates an instance of the Class named e.
e.a = 45 #Here, you're setting the instance attribute a to 45. Note that 
# this doesn't affect the class attribute a, but creates a new a specific 
# to the instance e.

e.name = "Divyansh Dubey"
print(e.fname, e.lname)

e.show() 
# Since show operates on the class, it accesses the class attribute a, 
# not the instance attribute.
# The output will show the class attribute a value, which is 1 
# (because the class attribute wasn't changed when you set e.a = 45).